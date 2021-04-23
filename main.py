# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#part 1
def greet(name: str, template: str = f'Hello, <name>!'):
          return template.replace('<name>', name)


#part2
def force(mass: float, body: str = 'earth'):
    gravities = {
    'sun': 274.0,
    'jupiter': 24.9,
    'neptune': 11.2,
    'saturn': 10.4,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6
    }
    
    if body not in gravities:
        return None 
    return format(mass * gravities[body], '.1f')

   

#part3
def pull(m1: float, m2: float, d: float):
    G = 6.674 * 10 ** -11
    return G*((m1 * m2)/d ** 2)

    
def main():
    print(greet('Doc'))
    print(greet('Bob', 'Whats up, <name>!'))

    print(force(1, 'earth'))

    print(pull(1000, 11000000, 2))

if __name__ == '__main__':
    main()
    
