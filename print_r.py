'''
Created on Aug 19, 2013

@author: mckenzie

This contains the function print_r, which is an attempt to replicate the exceedingly
useful function of the same name from PHP.  It is, and will remain until I get a lot better
at Python, under development, and may break for inexplicable reasons.
'''

def pr_item(row, indents=1):
    """Prints one line for print_r(), at the correct number of indents."""
    indent = "\t"
    print(indent*indents + row)

def print_r(input_var,base_indent=1):
    """Print the structure of a variable (string, number, list, tuple, or dict) in a human readable format."""
    # Simplify typing.
    bi = base_indent
    tab = "\t"
    # Get the type to be human readable.
    input_type = str(type(input_var))[8:-2]
    if bi == 1:
        print(input_type)
    
    # Now start printing stuff.
    if isinstance(input_var, str):
        pr_item(input_var,0)
        
    elif isinstance(input_var, int) or isinstance(input_var, float):
        # If you've got complex numbers, you're on your own.
        row = str(input_var)
        pr_item(row,bi+0)
        
    elif isinstance(input_var, list):
        print(tab*(bi-1) + "[")
        count = 0
        while count < len(input_var):
            
            if isinstance(input_var[count], list) or isinstance(input_var[count], tuple) or isinstance(input_var[count], dict):
                # This just got complicated.                
                row = "[" + str(count) + "] = " + str(type(input_var[count]))[8:-2]
                pr_item(row)
                print_r(input_var[count],bi+1)
            else:
                row = "[" + str(count) + "] = " + input_var[count]
                pr_item(row, bi)
            count = count + 1
        print(tab*(bi-1) + "]")
        
    elif isinstance(input_var, tuple):
        print(tab*(bi-1) + "(")
        count = 0
        while count < len(input_var):
            
            if isinstance(input_var[count], list) or isinstance(input_var[count], tuple) or isinstance(input_var[count], dict):
                # This just got complicated.                
                row = "(" + str(count) + ") = " + str(type(input_var[count]))[8:-2]
                pr_item(row)
                print_r(input_var[count],bi+1)
            else:
                row = "(" + str(count) + ") = " + input_var[count]
                pr_item(row, bi)
            count = count + 1
        print(tab*(bi-1) + ")")

    elif isinstance(input_var,dict):
        print(tab*(bi-1) + "{")
        for key in input_var:
            if isinstance(input_var[key], list) or isinstance(input_var[key], tuple) or isinstance(input_var[key], dict):
                # This just got complicated.                
                row = "{" + str(key) + "} = " + str(type(input_var[key]))[8:-2]
                pr_item(row)
                print_r(input_var[key],bi+1)
            else:
                row = "{" + str(key) + "} = " + input_var[key]
                pr_item(row, bi)
        print(tab*(bi-1) + "}")
        
    else:
        print("Object of unknown type was entered.  The type is " + str(type(input_var)))
    

if __name__ == "__main__":
    
    string_var = "This is a string."
    int_var = 75
    float_var = 7.5
    list_var = ['one','two', 'three']
    clist_var = ['1', '2', list_var]
    tuple_var = ('a', 'b', 'c')
    dict_var = {'foo': 'bar', 'fu': 'bahr'}


    test_var = clist_var
    

    print("Now, with the new improved print_r!")
    print_r(test_var)