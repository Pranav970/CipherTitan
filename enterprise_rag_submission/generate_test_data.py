import os
import json
import csv
from datetime import datetime, timedelta

def setup_directory_structure(base_dir="enterprise_vault"):
    """Creates the target directory silos for the enterprise data."""
    directories = [
        f"{base_dir}/documents",
        f"{base_dir}/structured",
        f"{base_dir}/logs",
        f"{base_dir}/security"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print(f"[✓] Initialized enterprise data silos under: {base_dir}/")

def generate_security_layers(base_dir="enterprise_vault"):
    """Generates user-role mappings and explicit file access policies."""
    user_roles = {
        "USR_001": {"name": "Sarah Jenkins", "department": "Executive", "role": "Admin"},
        "USR_002": {"name": "Alex Chen", "department": "Engineering", "role": "Engineering"},
        "USR_003": {"name": "Marcus Vance", "department": "Human Resources", "role": "HR"},
        "USR_004": {"name": "Elena Rostova", "department": "Operations", "role": "Guest"}
    }
    
    document_policies = {
        "HR_Policy_2026.txt": {"required_role": ["Admin", "HR", "Engineering", "Guest"]},
        "Q3_Project_Hyperion_Specs.txt": {"required_role": ["Admin", "Engineering"]},
        "FY2026_Q1_Financial_Report.txt": {"required_role": ["Admin"]}
    }
    
    with open(f"{base_dir}/security/user_roles.json", "w") as f:
        json.dump(user_roles, f, indent=4)
        
    with open(f"{base_dir}/security/document_policies.json", "w") as f:
        json.dump(document_policies, f, indent=4)
        
    print("[✓] Provisioned Role-Based Access Control (RBAC) security configurations.")

def generate_unstructured_docs(base_dir="enterprise_vault"):
    """Generates internal documents representing the unstructured data silo."""
    hr_content = (
        "ENTERPRISE STANDARD OPERATING PROCEDURE: WORKPLACE FLEXIBILITY (REVISION 2026)\n"
        "Document ID: DOC-HR-2026-01 | Classification: Public / Internal All\n\n"
        "1. Core Working Hours: All full-time employees must remain reachable between 10:00 AM and 3:00 PM EST.\n"
        "2. Remote Work Stipend: Employees are eligible for a maximum equipment reimbursement of $500 biennially.\n"
        "3. Leave Policy: Standard annual leave is allocation of 25 days, accruing monthly."
    )
    
    eng_content = (
        "PROJECT HYPERION: ARCHITECTURAL SPECIFICATION AND INGESTION SCHEMICS\n"
        "Document ID: DOC-ENG-2026-88 | Classification: Restricted (Engineering / Executive Only)\n"
        "Author: Lead Engineer Alex Chen (USR_002)\n\n"
        "Overview: Project Hyperion targets a microservices ingestion cluster handling up to 50,000 requests/sec.\n"
        "1. Database Architecture: We employ a primary-replica distributed cluster using PostgreSQL with vector extensions.\n"
        "2. Connection Endpoints: The internal secure gateway is hosted at hyperion-prod-mesh.internal.net:8443.\n"
        "3. Encryption: All payload data at rest must be processed with AES-256-GCM encryption layers."
    )
    
    fin_content = (
        "CONFIDENTIAL FINANCIAL RECORD: FY2026 Q1 PERFORMANCE SUMMARY\n"
        "Document ID: DOC-FIN-2026-03 | Classification: Strictly Confidential (Executives Only)\n\n"
        "1. Total Consolidated Revenue: Gross operational revenue for Q1 closed at $14,250,000.\n"
        "2. R&D Overhead Allocation: Investment into deep technical systems reached $4,120,000, driven heavily by Project Hyperion.\n"
        "3. Operating Margins: Adjusted operating margins stabilized at a calculated 28.4%."
    )
    
    docs = {
        "HR_Policy_2026.txt": hr_content,
        "Q3_Project_Hyperion_Specs.txt": eng_content,
        "FY2026_Q1_Financial_Report.txt": fin_content
    }
    
    for filename, content in docs.items():
        with open(f"{base_dir}/documents/{filename}", "w") as f:
            f.write(content)
            
    print(f"[✓] Authored {len(docs)} multi-classification enterprise documents.")

def generate_structured_data(base_dir="enterprise_vault"):
    """Generates corporate operational database dumps as CSVs."""
    employee_data = [
        ["employee_id", "name", "email", "department", "salary_tier"],
        ["USR_001", "Sarah Jenkins", "s.jenkins@enterprise.com", "Executive", "Tier-5"],
        ["USR_002", "Alex Chen", "a.chen@enterprise.com", "Engineering", "Tier-4"],
        ["USR_003", "Marcus Vance", "m.vance@enterprise.com", "Human Resources", "Tier-3"],
        ["USR_004", "Elena Rostova", "e.rostova@enterprise.com", "Operations", "Tier-2"]
    ]
    
    asset_data = [
        ["asset_id", "component_name", "vendor", "purchase_cost", "status"],
        ["AST-901", "High-Compute GPU Node Cluster", "NVIDIA Corp", "125000.00", "Deployed"],
        ["AST-902", "Secure Edge Load Balancer", "F5 Networks", "18500.00", "Deployed"],
        ["AST-903", "Backup SAN Array 100TB", "PureStorage", "45000.00", "Procurement"]
    ]
    
    with open(f"{base_dir}/structured/employees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(employee_data)
        
    with open(f"{base_dir}/structured/assets.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(asset_data)
        
    print("[✓] Extracted operational structured data dumps (employees.csv, assets.csv).")

def generate_semi_structured_logs(base_dir="enterprise_vault"):
    """Generates continuous system audit trails tracking cross-silo events."""
    base_time = datetime.now() - timedelta(days=2)
    
    logs = [
        {
            "timestamp": (base_time + timedelta(hours=2)).isoformat(),
            "event_id": "EVT-LOG-1092",
            "user_id": "USR_003",
            "action": "READ_DOCUMENT",
            "resource": "HR_Policy_2026.txt",
            "status": "SUCCESS",
            "ip_address": "10.194.22.105"
        },
        {
            "timestamp": (base_time + timedelta(hours=5)).isoformat(),
            "event_id": "EVT-LOG-1093",
            "user_id": "USR_002",
            "action": "READ_DOCUMENT",
            "resource": "Q3_Project_Hyperion_Specs.txt",
            "status": "SUCCESS",
            "ip_address": "10.194.40.12"
        },
        {
            "timestamp": (base_time + timedelta(hours=14)).isoformat(),
            "event_id": "EVT-LOG-1094",
            "user_id": "USR_004",
            "action": "READ_DOCUMENT",
            "resource": "Q3_Project_Hyperion_Specs.txt",
            "status": "ACCESS_DENIED",
            "ip_address": "10.194.88.219",
            "reason": "Insufficient role privileges. Required: Admin or Engineering. User role: Guest"
        },
        {
            "timestamp": (base_time + timedelta(hours=26)).isoformat(),
            "event_id": "EVT-LOG-1095",
            "user_id": "USR_001",
            "action": "EXPLICIT_EXPORT",
            "resource": "FY2026_Q1_Financial_Report.txt",
            "status": "SUCCESS",
            "ip_address": "10.194.10.5"
        }
    ]
    
    with open(f"{base_dir}/logs/system_audit.json", "w") as f:
        json.dump(logs, f, indent=4)
        
    print("[✓] Compiled system operational logs (system_audit.json) including failure payloads.")

if __name__ == "__main__":
    print("=== STARTING DATA SYNTHESIS FOR ENTERPRISE CHALLENGE ===")
    setup_directory_structure()
    generate_security_layers()
    generate_unstructured_docs()
    generate_structured_data()
    generate_semi_structured_logs()
    print("=== DATA INGESTION PREPARATION COMPLETE ===")
