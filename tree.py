
class Node():

    def __init__(self, evaluation:int) -> None:
        self.leftchild = None
        self.rightchild = None
        self.evaluation = evaluation
    
    def __init__(self, leftchild, rightchild) -> None:
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.evaluation = 0
    
    def __repr__(self) -> str:
        while self.leftchild is not None:
            return f"{self.evaluation}\n /  \ \n{self.leftchild}   {self.rightchild}"

def main():
    t1, t2, t3, t4 = Node(1), Node(2), Node(3), Node(4)
    t5 = Node(t1, t2)
    t6 = Node(t3, t4)
    t = Node(t5, t6)
    print(t)

if __name__ == "__main__":
    main()    
