Maintenance and Troubleshooting
===============================

This section provides guidelines for maintaining MindMira and resolving common issues.

Routine Maintenance
-------------------

1. **Dependency Updates**:
   - Regularly update Python packages to ensure compatibility:
     ```bash
     pip install --upgrade -r requirements.txt
     ```

2. **Log Management**:
   - Clear old logs periodically to save storage space:
     - Logs are stored in the `logs/` directory.
     - Use the following command to remove logs older than 30 days:
       ```bash
       find logs/ -type f -mtime +30 -delete
       ```

3. **Database Backup**:
   - If using a database, back up your SQLite database regularly:
     ```bash
     cp data/mindmira.db backups/mindmira_backup_$(date +%F).db
     ```

Troubleshooting Common Issues
-----------------------------

1. **Chatbot Fails to Start**:
   - **Problem**: Missing dependencies.
   - **Solution**: Reinstall dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Emotion Analysis Not Working**:
   - **Problem**: Missing or outdated NLP libraries.
   - **Solution**: Ensure `TextBlob` or `NLTK` is installed and up to date:
     ```bash
     pip install --upgrade textblob nltk
     ```

3. **Slow Response Time**:
   - **Problem**: High system load or outdated configuration.
   - **Solution**:
     - Reduce the `response_speed` setting in `config.json` to `"fast"`.
     - Restart the chatbot to apply changes:
       ```bash
       python chatbot.py
       ```

4. **Error Logs**:
   - Errors are logged in `logs/error.log`. Check this file for detailed error messages.

Contact for Support
-------------------

For additional support, reach out to the MindMira development team:
- **Email**: support@mindmira.com
- **Community Forum**: [GitHub Discussions](https://github.com/MindMira/MindMira/discussions)
