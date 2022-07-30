# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        a=l1.val
        
        b=l2.val
        mult1=10
        mult2=10
        while l1.next !=None:
            a=l1.next.val*mult1+a
            mult1=mult1*10
            
            l1=l1.next
        while l2.next !=None:
            b=l2.next.val*mult2+b
            mult2=mult2*10
            
            l2=l2.next
        
        c= str(a+b)
        
        l3=ListNode(c[len(c)-1])
        nexs=l3.next
        leng=len(c)-1-1
        while leng >=0:
            
            while nexts is not None:
                
                nexts=nexts.next
            print(l3.val,"val")
            newNode=ListNode(c[leng])
            print(newNode)
            l3.next=newNode
            print(l3)
            leng-=1
       
      
     
        
        