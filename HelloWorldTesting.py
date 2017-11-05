from HelloWorld import HelloWorld


def test_hello_world():
   cn=HelloWorld()
   assert(cn.print_messge() == "hello world !")
