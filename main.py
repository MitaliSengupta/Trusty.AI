#Main method
#Project truty.ai, DoraHacks hackathon

#importing random for random()
import random

#importing functions
import excScore
import captLog
import pldChoices
import blockchain
import datetime
import hashlib
import time

#Creating data array
print("****************************************  **************")
print("*************************************  ****  ***********")
print("****************************************  **************")
print("********************************************************")
print("***********TRUSTY AI algorithm started!*****************")
print("********************************************************")
print("************  ******************************************")
print("*******  ********  *************************************")
print("************  ******************************************")
print("*********  ****  ***************************************")
print("********************************************************")
print("********************************************************")

#Creating classes for blockchain
class Message:
        def __init__(self, data):
                self.hash = None
                self.prev_hash = None
                self.timestamp = time.time()
                self.size = len(data.encode('utf-8'))   # length in bytes
                self.data = data
                self.payload_hash = self._hash_payload()

        def _hash_payload(self):
                return hashlib.sha256(bytearray(str(self.timestamp) + str(self.data), "utf-8")).hexdigest()

        def _hash_message(self):
                return hashlib.sha256(bytearray(str(self.prev_hash) + self.payload_hash, "utf-8")).hexdigest()

        def link(self, message):
                """ Link the message to the previous one via hashes."""
                self.prev_hash = message.hash

        def seal(self):
                """ Get the message hash. """
                self.hash = self._hash_message()

        def validate(self):
                """ Check whether the message is valid or not. """
                if self.payload_hash != self._hash_payload():
                        raise InvalidMessage("Invalid payload hash in message: " + str(self))
                if self.hash != self._hash_message():
                        raise InvalidMessage("Invalid message hash in message: " + str(self))

        def __repr__(self):
                return 'Message<hash: {}, prev_hash: {}, data: {}>'.format(
                        self.hash, self.prev_hash, self.data[:20]
                )


class Block:
        def __init__(self, *args):
                self.messages = []
                self.timestamp = None
                self.prev_hash = None
                self.hash = None
                if args:
                        for arg in args:
                                self.add_message(arg)

        def _hash_block(self):
                return hashlib.sha256(bytearray(str(self.prev_hash) + str(self.timestamp) + self.messages[-1].hash, "utf-8")).hexdigest()

        def add_message(self, message):
                if len(self.messages) > 0:
                        message.link(self.messages[-1])
                message.seal()
                message.validate()
                self.messages.append(message)

        def link(self, block):
                """ The block hash only incorporates the head message hash
                        which then transitively includes all prior hashes.
                """
                self.prev_hash = block.hash

        def seal(self):
                self.timestamp = time.time()
                self.hash = self._hash_block()

        def validate(self):
                """ Validates each message hash, then chain integrity, then the block hash.
                        Calls each message's validate() method.

                        If a message fails validation, this method captures the exception and
                        throws InvalidBlock since an invalid message invalidates the whole block.
                """
                for i, msg in enumerate(self.messages):
                        try:
                                msg.validate()
                                if i > 0 and msg.prev_hash != self.messages[i - 1].hash:
                                        raise InvalidBlock(
                                            "Invalid block: Message #{} has invalid message link in block: {}".format(i, str(self)))
                        except InvalidMessage as ex:
                                raise InvalidBlock("Invalid block: Message #{} failed validation: {}. In block: {}".format(
                                        i, str(ex), str(self))
                                )

        def __repr__(self):
                return 'Block<hash: {}, prev_hash: {}, messages: {}, time: {}>'.format(
                        self.hash, self.prev_hash, self.messages, self.timestamp
                )


class SimpleChain:
        def __init__(self):
                self.chain = []

        def add_block(self, block):
                """ Add a block if valid."""
                if len(self.chain) > 0:
                        block.prev_hash = self.chain[-1].hash
                block.seal()
                block.validate()
                self.chain.append(block)

        def validate(self):
                """ Validates each block, in order.
                        An invalid block invalidates the chain.
                """
                for i, block in enumerate(self.chain):
                        try:
                                block.validate()
                        except InvalidBlock as exc:
                                raise InvalidBlockchain(
                                    "Invalid blockchain at block number {} caused by: {}".format(i, str(exc)))
                return True

        def __repr__(self):
                return 'SimpleChain<blocks: {}>'.format(len(self.chain))


class InvalidMessage(Exception):
        def __init__(self, *args, **kwargs):
                Exception.__init__(self, *args, **kwargs)


class InvalidBlock(Exception):
        def __init__(self, *args, **kwargs):
                Exception.__init__(self, *args, **kwargs)


class InvalidBlockchain(Exception):
        def __init__(self, *args, **kwargs):
                Exception.__init__(self, *args, **kwargs)

#blockchain function
def blockchain_fun():
    if __name__ == "__main__":
                    chain = SimpleChain()
                    block = Block()
                    index = 0
                    print("Please, re-enter the same input for " + name + " to validate through the blockchain: ")
                    block.add_message(Message(input()))
                    if len(block.messages) > 0:
                            chain.add_block(block)
                            block = Block()
                            if len(chain.chain) > 0:
                                    try: print(chain.chain[index].messages)
                                    except: print("The block does not exist at this location.")
                            print("*******************")
                            print("Current chain:")
                            print("******************")
                            for b in chain.chain:
                                print(b)
                            print("----------------")
                            if chain.validate(): print("Integrity validated.")
                    else: print("Block is empty, try adding some messages")

#Seeindg data with 0's
num_people = 6
data = [['Austin',0,0,0,0,0], ['Sidney',0,0,0,0,0], ['Becky',0,0,0,0,0], 
['Andrew',0,0,0,0,0], ['Kevin',0,0,0,0,0], ['Mitali',0,0,0,0, 0]]

#Seeing data with student names via input
for i in range(num_people):
    print("Please enter the name for student {i}:".format(**locals()))
    data[i][0] = input() 
    name = data[i][0]
    print("                                              ")
    print("**********************************************")
    print("           Student {i} added as {name}".format(**locals()))
    print("**********************************************")
    print("                                              ")

#Print all studnets to verify
print("Current Student Pool:")
print("*****************")
for studentPrint in range(num_people):
    print(data[studentPrint])

#Creating weighted array for later
weight_arr = [1, 1, 1]

#Implement AI function
wrand = [1, 1, 1]
wrand[0] = weight_arr[0] * random.randrange(90000,110000)/100000
wrand[1] = weight_arr[1] * random.randrange(90000,110000)/100000
wrand[2] = weight_arr[2] * random.randrange(90000,110000)/100000

print("***************************************************************")
print("Please begin entering # of people and average exercise scores:")
print("***************************************************************")
#Getting score
for gettingScores in range(num_people):
    name = data[gettingScores][0]
    cap_score = captLog.cap_log(name) * wrand[0] / (data[gettingScores][2] + 1)
    score = excScore.exer_score(name) * wrand[0] / (data[gettingScores][2] + 1)
    print("****************************************************************")
    pld_score = (10 - data[gettingScores][2]) * wrand[0] / (data[gettingScores][2]+1)
    data[gettingScores][4] = cap_score + score + pld_score 

#Creating chocies store
choices = pldChoices.pld_choices(data)

#Printing choices and changes PLD average
print("<*********************>")
print("<****MATCH FOUND!*****>")
print("<*********************>")
print("The LEAD is: " + data[choices[0]][0])
print("The ASSISTANT is: " + data[choices[1]][0])
print("<*********************>")
print("<*********************>")
print("<*********************>")

#Setting initial Target/Error to 0
error = 0
sum = 0
for leadChoice in range(num_people):
    name = data[choices[0]][0]
    print("Enter Lead PLD review of " + name + " for AI: ")
    index = int(input())
    #calling blockchain
    blockchain_fun()
    sum += index
   
data[choices[0]][1] = (data[choices[0]][1] + sum)/(data[choices[0]][1]+1)
error += sum;
sum = 0
print("****************Now Review******************")
for assitantChoice in range(num_people):
    name = data[choices[1]][0]
    print("Enter Assitant PLD review of " + name + " for AI: ")
    index = int(input())
    #calling blockchain
    blockchain_fun()
    sum+= index
    

data[choices[1]][1] = (data[choices[1]][1] + sum)/(data[choices[1]][1]+1)
error += sum

#Checking for target/error for AI, more magic happens
if error > 0:
    for sendMemory in weight_arr:
        sendMemory = int(sendMemory)
        print("Results before ----> INPUT:")
        print(weight_arr)
        weight_arr[sendMemory] = weight_arr[sendMemory] + (weight_arr[sendMemory] - wrand[sendMemory]) * .9
        print("Results after ----> OUTPUT:")
        print(weight_arr)
        print("<*********************>")
        print("<******TARGET*********>")
        print("<*********MET*********>")
        print("<**********RESULTS****>")
        print("<************ADJUSTED*>")
        print("<*********************>")

              
else:
    for sendMemory in weight_arr:
        sendMemory = int(sendMemory)
        print("Results before ----> INPUT:")
        print(weight_arr)
        weight_arr[sendMemory] = weight_arr[sendMemory] - (weight_arr[sendMemory] - wrand[sendMemory]) * 1.1
        print("Results after ----> OUTPUT:")
        print(weight_arr)
        print("<*********************>")
        print("<******ERROR**********>")
        print("<*********MET*********>")
        print("<**********RESULTS****>")
        print("<************ADJUSTED*>")
        print("<*********************>")
    
print("****************************************  **************")
print("*************************************  ****  ***********")
print("****************************************  **************")
print("********************************************************")
print("***********TRUSTY AI algorithm LEARNED!*****************")
print("********************************************************")
print("************  ******************************************")
print("*******  ********  *************************************")
print("************  ******************************************")
print("*********  ****  ***************************************")
print("********************************************************")
print("********************************************************")