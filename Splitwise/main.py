"""
1. Add/remove user
2. Create/remove groups
3. Split expenses equally
4. Do group expenses with specific members
5. Code should be scalable such that if we want to implement custom split expenses, we can add without hassle.
6. Settle expenses user to user and user to group
7. Show balances for all user
"""

from abc import ABC, abstractmethod
from collections import defaultdict


# User represents a user with balance owed to other people
class User:
    def __init__(self, user_id, name) -> None:
        """
        self.balance is the balance for the current user where other users owe (+ve) or lent (-ve) money
        balance = {
            user1_id: 100,
            user2_id: 200,
            user3_id: -150
        }
        """
        self.id = user_id
        self.name = name
        self.balance = defaultdict(int)


# Group represents a group of User objects in members set
class Group:
    def __init__(self, group_id, name) -> None:
        self.id = group_id
        self.name = name
        # we can add the users to the group.members
        self.members = set()

    def add_member(self, user):
        if user not in self.members:
            self.members.add(user)

    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)


# Expense represents individual expenses in splitwise, can be represented in form of a dict {user_id: amount to pay the person who paid}
class Expense(ABC):
    def __init__(self, amount, paid_by, participants) -> None:
        """
        participants: User[]
        paid_by: User 
        """
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants

    @abstractmethod
    def split(self):
        pass


# EqualSplit is a splitting strategy where we divide the amount equal amongst all participants
class EqualSplitExpense(Expense):
    def __init__(self, amount, paid_by, participants) -> None:
        super().__init__(amount, paid_by, participants)

    def generate_expense(self):
        """
        Generate expense dict {user_id: money_owed}
        """
        individual_expense = self.amount / len(self.participants)
        expense_dict = {}
        for participant in self.participants:
            if participant.id != self.paid_by.id:
                expense_dict[participant.id] = individual_expense
        return expense_dict
                


class ExpenseFactory:
    @staticmethod
    def create_expense(split_strat, amount, paid_by, participants):
        if split_strat == "equal":
            return EqualSplitExpense(amount, paid_by, participants)
        


class Splitwise:
    def __init__(self) -> None:
        """
        users, groups, and expenses are array of the respective objects
        """
        self.users = {}
        self.groups = {}
        self.expenses = []

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def create_group(self, group_id, name):
        if group_id not in self.groups:
            self.groups[group_id] = Group(group_id, name)

    def remove_group(self, group_id):
        if group_id in self.groups:
            del self.groups[group_id]

    def add_user_to_group(self, user_id, group_id):
        if user_id in self.users and group_id in self.groups:
            self.groups[group_id].add_member(self.users[user_id])

    def remove_user_from_group(self, user_id, group_id):
        if user_id in self.users and group_id in self.groups:
            del self.groups[group_id].remove_member(self.users[user_id])
    
    def add_expense(self, split_strat, amount, paid_by_id, participant_ids: list):
        """
        Add expense object to the expense list
        """
        paid_by = self.users[paid_by_id]
        participants = [self.users[participant_id] for participant_id in participant_ids]
        expense = ExpenseFactory.create_expense(split_strat, amount, paid_by, participants)
        self.expenses.append(expense)

    def compute_expense(self, expense):
        """
        Compute the expense and add or subtract the money owed for a user. Basically, everytime we add a 
        new expense to our expense list, we compute the amount owed for the users involved in the expense
        and update it.
        """
        paid_by_id = expense.paid_by.id
        expense_dict = expense.generate_expense()

        for user_id, amount in expense_dict.items():
            self.users[paid_by_id].balance[user_id] += amount   
            self.users[user_id].balance[paid_by_id] -= amount 
        
    def settle_expense(self, user1_id, user2_id):
        if user1_id in self.users and user2_id in self.users:
            user1 = self.users[user1_id]
            user2 = self.users[user2_id]
            
            if user1_id in user2.balance and user1_id in user2.balance:
                user1.balance[user2_id] = 0
                user2.balance[user1_id] = 0