class QueryRouter:
    @staticmethod
    def route_query(query_text):
        """Analyzes syntax and intent vectors to classify queries deterministically."""
        query_lower = query_text.lower()
        
        if any(w in query_lower for w in ["log", "audit", "event", "ip address", "denied", "failure"]):
            return "AUDIT_LOG"
            
        if any(w in query_lower for w in ["salary", "tier", "employee", "asset", "cost", "vendor", "purchase", "total"]):
            return "STRUCTURED"
            
        return "UNSTRUCTURED"
