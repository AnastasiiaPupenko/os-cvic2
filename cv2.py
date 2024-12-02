def to_infix(postfix):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in postfix.split():
        if token in operators:
          
            b = stack.pop()
            a = stack.pop()
            expression = f"( {a} {token} {b} )"
            stack.append(expression)
        else:
            stack.append(token)
    
    return stack[0]

def to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = []
    
    for token in infix.split():
        if token.isdigit():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)
    
    while stack:
        result.append(stack.pop())
    
    return ' '.join(result)

#to_infix
print(to_infix("1 2 *"))         
print(to_infix("1 2 * 3 +"))      
print(to_infix("1 2 3 * +"))      
print(to_infix("1"))             

# to_postfix
print(to_postfix("1"))
print(to_postfix("( 1 + 2 )"))             
print(to_postfix("( 10 * ( 1 + 2 ) )"))     
print(to_postfix("( ( 10 + 1 ) * ( 2 / 3 ) )"))   