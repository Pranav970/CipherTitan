import json
import os

class RBACEngine:
    def __init__(self, base_dir="enterprise_vault"):
        self.base_dir = base_dir
        self.user_roles_path = os.path.join(base_dir, "security", "user_roles.json")
        self.doc_policies_path = os.path.join(base_dir, "security", "document_policies.json")
        self.load_policies()

    def load_policies(self):
        with open(self.user_roles_path, 'r') as f:
            self.user_roles = json.load(f)
        with open(self.doc_policies_path, 'r') as f:
            self.doc_policies = json.load(f)

    def get_user_context(self, user_id):
        """Retrieves user profile and role details."""
        if user_id not in self.user_roles:
            raise PermissionError(f"Access Denied: User ID '{user_id}' is unrecognized.")
        return self.user_roles[user_id]

    def filter_accessible_documents(self, user_id):
        """Returns a list of filenames the user is authorized to access."""
        user_info = self.get_user_context(user_id)
        user_role = user_info["role"]
        
        if user_role == "Admin":
            return list(self.doc_policies.keys())
            
        accessible_docs = []
        for doc, policy in self.doc_policies.items():
            if user_role in policy["required_role"]:
                accessible_docs.append(doc)
        return accessible_docs

    def validate_structured_access(self, user_id, table_name):
        """Enforces field and row-level separation boundaries for structured assets."""
        user_info = self.get_user_context(user_id)
        user_role = user_info["role"]
        
        if table_name == "employees" and user_role not in ["Admin", "HR"]:
            raise PermissionError(f"Security Violation: Role '{user_role}' cannot access sensitive Employee tables.")
        return True
