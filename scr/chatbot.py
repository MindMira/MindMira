import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import Document
import pandas as pd
import os

# 환경 변수 설정
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# Streamlit 제목
st.title('Transformer 기반 RAG 챗봇')

# 사용자 정보 입력
user_name = st.text_input("이름을 입력하세요:")
user_age = st.number_input("나이를 입력하세요:", min_value=0, step=1)
user_gender = st.selectbox("성별을 선택하세요:", ("남자", "여자", "선택 안 함"))

if user_name and user_age and user_gender:
    st.write(f"안녕하세요, {user_name}님! ({user_age}세, {user_gender})")

    # 법률 정보 벡터 DB 로드 함수
    def load_vector_db():
        try:
            df = pd.read_csv("law_data.csv")  # 법률 정보 데이터 불러오기
            documents = [
                Document(
                    page_content=f"질문: {row['Text']}\n답변: {row['Completion']}", 
                    metadata={"source": f"row_{i}"}
                ) 
                for i, row in df.iterrows()
            ]

            model_name = "sentence-transformers/LaBSE"
            embeddings = HuggingFaceEmbeddings(model_name=model_name)
            vectors = FAISS.from_documents(documents, embeddings)
            return vectors
        except FileNotFoundError:
            st.error("법률 정보 데이터 파일을 찾을 수 없습니다. 'law_data.csv' 파일을 확인하세요.")
            return None
        except Exception as e:
            st.error(f"벡터 DB 로드 중 오류가 발생했습니다: {e}")
            return None

    # 벡터 DB 로드
    vector_db = load_vector_db()

    if vector_db is None:
        st.stop()

    # 트랜스포머 모델 로드
    try:
        tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-nq")
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/rag-token-nq")
    except Exception as e:
        st.error(f"모델 로드 중 오류가 발생했습니다: {e}")
        st.stop()

    # 질문 처리 함수 정의
    def chat(query):
        try:
            inputs = tokenizer(query, return_tensors="pt")
            outputs = model.generate(**inputs)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return result
        except Exception as e:
            st.error(f"챗봇 응답 생성 중 오류가 발생했습니다: {e}")
            return "오류가 발생했습니다. 다시 시도해주세요."

    # 대화 기록 초기화
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # 대화 컨테이너
    response_container = st.container()
    container = st.container()

    with container:
        with st.form(key='Chat_Question', clear_on_submit=True):
            user_input = st.text_input("질문을 입력하세요:", placeholder="법률이나 심리 상담에 대해 물어보세요.", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            output = chat(user_input)

            # 대화 기록 업데이트
            st.session_state['history'].append({"user": user_input, "assistant": output})

    if st.session_state['history']:
        with response_container:
            for entry in st.session_state['history']:
                st.write(f"사용자: {entry['user']}")
                st.write(f"챗봇: {entry['assistant']}")
else:
    st.write("사용자 정보를 모두 입력해 주세요.")
