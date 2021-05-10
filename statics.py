class keycloak:
    def __str__(self):
        return self
    
    def __init__(self):
        self.configuration = configuration()
        
        
class configuration(keycloak):
    def __str__(self):
        return self

    def __init__(self, *args, **kwargs):
        self.roles = 'roles'

class spec:
    def __init__(self):
        self.id = 'id'
        self.name = 'name'
        self.description = 'description'
        
class composite:
    def __init__(self):
        self.composite = 'composite' 
        self.composites = 'composites'
               

class roles(spec):
    def __str__(self):
        return self
    
    def __init__(self, *args, **kwargs):
        super(spec, self).__init__(*args, **kwargs)
        self.clientRole = 'clientRole'
        self.attributes = 'attributes'
        self.containerId = 'containerId'

class realm(roles, composite):
    def __str__(self):
        return self
    
    def __init__(self, *args, **kwargs):
        super(roles, self).__init__(*args, **kwargs)
        super(composite, self).__init__(*args, **kwargs)
        
class client(roles, composite):
    def __str__(self):
        return super(roles).__str__()
    
    def __init__(self, *args, **kwargs):
        super(roles, self).__init__(*args, **kwargs)
        super(composite, self).__init__(*args, **kwargs)
        
class realm_management(client, composite):
    def __str__(self):
        return 'realm-management'
    
    def __init__(self, *args, **kwargs):
        super(client).__init__(*args, **kwargs)
        
class broker(client, composite):
    def __str__(self):
        return self
    
    
    def __init__(self, *args, **kwargs):
        super(client, self).__init__(*args, **kwargs)
        super(composite, self).__init__(*args, **kwargs)
        
class account(client, composite):
    def __str__(self):
        return self
    
    def __init__(self, *args, **kwargs):
        super(client, self).__init__(*args, **kwargs)
        super(composite, self).__init__(*args, **kwargs)
        
class groups(roles):
    def __str__(self):
        return self
    
    
    def __init__(self, *args, **kwargs):
        super(roles, self).__init__(*args, **kwargs)
        self.path = 'path'
        self.clientRoles = 'clientRoles'
        self.realmRoles = 'realmRoles'
        self.subGroups = 'subGroups'
      
        