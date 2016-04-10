__author__ = 'Prisma Overlord'
#Open XSPACE config File
import itertools

import os
import sys, getpass, cmd, datetime
import lib

class BSTNode:
    """
    Implementation for the node of Binary Search Tree
    """
    def __init__(self, key, value, parent=None, left=None, right=None):
        """
        The Class Constructor.

        @:param key: the key of the node.
        @:param value: the value of the node.
        @:param parent: pointer to the parent node
        @:param left: pointer to the left child
        @:param right: pointer to the right child

        @return null
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
class binaryST:
    """
    Implementation of Binary Search Trees
    """
    def __int__(self):
        self.root = None
    def find_recursive(self,node,key):
        """
        Search the key from the node, recursively.

        :param node:
        :param key:
        :return:
        """
        if None == node or key == node.key:
            return node
        elif key < node.key:
            return self.find_recursive(node.left,key)
        else:
            return self.find_recursive(node.right,key)

    def find_iterative(self, node, key):
        """
        Search the key from node iteratively
        :param node: a BST node
        :param key: a key value
        :return: the node with the key; null if the key not found.
        """
        current_node = node
        while current_node:
            if key == current_node.key:
                return current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    def search(self, key):
        """
        Find the node with the key
        :param key: the target key
        :return: the node with the key; null if key not found.
        """
        return self.find_iterative(self.root,key)

    def insert(self, key, value):
        """
        Insert the (key,value) to the BST
        :param key: the key to insert
        :param value: the value to insert
        :return: True if inserted correctly; other wise, return false.
        """

        if None == self.root:
            self.root = BSTNode(key,value)
            return True
        current_node = self.root
        while current_node:
                if key == current_node.key:
                    print("The key does exist!")
                    return False
                elif key < current_node.key:
                    if current_node.left:
                            current_node = current_node.left
                    else:
                        current_node.left = BSTNode(key, value, current_node)
                        return True
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = BSTNode(key,value,current_node)
                        return True
    def replace_node(self, node,new_node):
        """
        Repalce the new node by new_node, update in its parent node
        :param node: The node to remove.
        :return: null
        """
        #Special Case: Replace the root.
        if node == self.root :
            self.root = new_node
            return
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print("Incorrect Parent-Child relation!")
            raise RuntimeError
    def remove_node(self,node):
        """
        Remove the node from the tree.
        :param none: the node to remove
        :return: null
        """
        if node.left.node.right:    #Node has two children.
            #Find its in order successor
            successor = node.right
            while successor.left:
                successor = successor.left
            #copy the node
            node.key = successor.key
            node.value = successor.value
            #remove the successor
            self.remove_node(successor)
        elif node.left: #The node only has a left child.
            self.replace_node(node,node.left)
        elif node.right: #The node only has a right child.
            self.replace_node(node,node.right)
        else:
            self.replace_node(node, None)
    def delete(self, key):
        """
        Delete the node with the key
        :param key:
        :return:True if the node is deleted successfully; otherwise false.
        """
        node = self.search(key)
        if node:
            self.remove_node(node)
class Application():



    num1 = 56
    num2 = 10

    def add(self,num1,num2):
        answer = num1+num2
        return answer





class shellEnvironment(cmd.Cmd):
    """
    Initialization of environment class.
    """
    intro = 'Welcome to the XSPACE-3D ENVIRONMENT SHELL. Type help or ? to list commands. \n'
    prompt = 'xspace~>:'
    file = "config.txt"
    GLOBAL_OBJECT_DB = binaryST()

    #Basic Environment Commands.
    @classmethod
    def sysInfo(cls):
        buildIndicator = "0.1"
        print("XSPACE 3D ENVIRONMENT v."+buildIndicator)
        print("OS Platform: "+sys.platform+"\nUser: "+getpass.getuser())
    #---- record and playback ----#
    def do_record(self, arg):
        'Save future commands to file name: RECORD rose.cmd'
        self.file = open(arg,"w")
    def do_playback(self, arg):
        try:
            'Playback commands from a file: PLAYBACK rose.cmd'
            self.close()
            with open(arg) as f:
                self.cmdqueue.extend(f.read().splitlines())
        except:
            FileNotFoundError
            print("Error! Can't find main config file. ")
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def do_createObj(self,arg):

        self.prompt("Enter name for this object:")
        newObject = Object(parse(arg),0)
        binaryST.insert(newObject)

class Object:
    def __init__(self, name, objID,x_pos,y_pos,z_pos,scale):
        self.name = name
        self.objID = objID
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.scale = scale
        referenceName = None
    def setName(self,name):
        self.name = name
    def setScale(self,scale):
        self.scale = scale
    def setXPosition(self,x_pos):
        self.x_pos = x_pos
    def setYPosition(self,y_pos):
        self.y_pos = y_pos
    def setZPosition(self,z_pos):
        self.z_pos = z_pos
    def setReferenceName(self,referenceName):
        self.referenceName = referenceName
    def getName(self,name):
        return name
    def getScale(self,scale):
        return scale
    def getXPosition(self,x_pos):
        return x_pos
    def getYPosition(self,y_pos):
        return y_pos
    def getZPosition(self,z_pos):
        return z_pos
    def getReferenceName(self,referenceName):
        return referenceName


env = shellEnvironment
env.sysInfo()
app = Application
def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
if __name__ == '__main__':

    env().cmdloop()


