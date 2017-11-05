class HelloWorld:

    def __init__(self):
        self.message = "hello world !"


    def print_messge(self):
        return self.message

if __name__ == '__main__':
    ob=HelloWorld()
    print(ob.print_messge())
