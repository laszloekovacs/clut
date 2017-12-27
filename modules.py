#import as a namespace
import greet
greet.sayHello('mike')

#import only one function
from greet import sayGoodbye

sayGoodbye('charlie')
