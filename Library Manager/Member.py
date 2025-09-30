class Member:
        def __init__(self, name, member_id):
                self._name= name
                self._member_id= member_id
                self.borrowedBook=[]
        def getMemberId(self):
                return self._member_id
        def getMemberName(self):
                return self._name
        def data(self):
                return f"{self._name:<15}{self._member_id:<10}"
        @staticmethod
        def title() :
                return f"{'Name':<15}{'ID':<10}{'Current Loans':<10}"
        