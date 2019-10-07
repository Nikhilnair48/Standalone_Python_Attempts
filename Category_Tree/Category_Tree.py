class Category:
    
    def __init__(self):
        self.value = None
        self.leftCategory = None
        self.rightCategory = None
       
    def __init__(self, val, leftCat, rightCat):
        self.value = val
        self.leftCategory = leftCat
        self.rightCategory = rightCat
        
    def get_value(self):
        return self.value
   
    def set_value(self, newVal):
        self.value = newVal
        
    def get_left_category(self):
        return self.leftCategory
    
    def set_left_category(self, newCategory):
        self.leftCategory = newCategory
        
    def get_right_category(self):
        return self.rightCategory
    
    def set_right_category(self, newCategory):
        self.rightCategory = newCategory
        
class CategoryTree:

    def __init__(self):
        self.root = None

    # NON-RECURSIVE SEARCH
    def search_category(self, category_val):
        if(self.root is None): return None

        category = self.root
        # SEARCH LEFT
        while True:
            
            # COULDN'T FIND IT
            if category is None: return None
            if category.get_value() is category_val:
                break
            else:
                category = category.get_left_category()

        # SEARCH RIGHT
        if category is None or category.get_value() is not category_val:
            category = self.root
            while True:
                # COULDN'T FIND IT
                if category is None: return None
                if category.get_value() is category_val:
                    break
                else:
                    category = category.get_right_category()

        return category

    def add_category(self, category, parent):
        
        # ADDING ROOT
        if(parent is None and self.root is None):
            self.root = Category(category, None, None)
        else:
            parent_node = self.search_category(parent)
            if(parent_node is None):
                raise KeyError("Parent node does not exist.")

            if(parent is self.root.value):
                if(self.root.get_left_category() is None):
                    self.root.set_left_category(Category(category, None, None))
                elif(self.root.get_right_category() is None):
                    self.root.set_right_category(Category(category, None, None))
                else:
                    raise KeyError("Number of children for the parent max: 2.")
                    
    def get_children(self, parent):
        if(parent is not None):
            parent_category = self.search_category(parent)
            self.get_children_helper(parent_category, parent_category)

    def get_children_helper(self, parent_category, exclude_category):
        if(parent_category is not None):
            self.get_children_helper(parent_category.get_left_category(), exclude_category)
            if(parent_category.get_value() is not exclude_category.get_value()):
                print(parent_category.get_value())
            self.get_children_helper(parent_category.get_right_category(), exclude_category)

c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(c.search_category('B'))
print(','.join(c.get_children('A') or []))