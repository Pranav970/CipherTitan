import os
import csv
import json

class DataIngestionPipeline:
    def __init__(self, base_dir="enterprise_vault"):
        self.base_dir = base_dir

    def fetch_unstructured_docs(self, allowed_files):
        """Loads and processes documents that match pre-filtered access lists."""
        docs_payload = {}
        doc_dir = os.path.join(self.base_dir, "documents")
        
        for file in allowed_files:
            file_path = os.path.join(doc_dir, file)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    docs_payload[file] = f.read()
        return docs_payload

    def query_csv_table(self, table_name):
        """Reads relational enterprise files from disk."""
        file_path = os.path.join(self.base_dir, "structured", f"{table_name}.csv")
        data = []
        if os.path.exists(file_path):
            with open(file_path, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(dict(row))
        return data

    def fetch_json_logs(self):
        """Loads historical system audit logs."""
        log_path = os.path.join(self.base_dir, "logs", "system_audit.json")
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                return json.load(f)
        return []
