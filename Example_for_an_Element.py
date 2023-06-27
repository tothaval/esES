class element(ES):
    def __init__(self):
        super().__init__()
        
        self.adress = 0
        
        self.rank = ES.element
        self.dynasty = "ElementSyntax"
        
        self.unique_id = -2
        self.name = "element"
        self.x = 0
        self.y = 0
        self.z = 0
        self.text = ""
        
        self.values = []
        self.references = {}
        
        self.initial_modifiers = [
            "?ElementSyntax?!last",
            "?ElementSyntax?!known",
            "?ElementSyntax?!neglect"
        ]
        
        self.modifiers = []
        
        self.connection_status = "neglect_connection"
    
    def get_connection_status(self):
        return self.connection_status
    
    def get_rank(self):
        return self.rank
    
    def get_dynasty(self):
        return self.dynasty
        
    def get_unique_id(self):
        return self.unique_id
        
    def get_name(self):
        return self.name
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
        
    def get_z(self):
        return self.z
        
    def get_text(self):
        return self.text
        
    def get_values(self):
        return self.values
        
    def get_references(self):
        return self.references
        
    def get_modifiers(self):
        return self.modifiers    

    def request_storage(self, list_idf, index_val):
        if list_idf is not None && if index_val > -1:
            references.update{{list_idf : index_val}}
            
            self.set_connection_status("accept_connection")
            
    def set_connection_status(self, new_connection_status):
        self.connection_status = new_connection_status
    
