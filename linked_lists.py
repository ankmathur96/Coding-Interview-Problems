class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def delete_node(self, i):
        if i > len(self):
            raise IndexError('Linkedlist Index out of Range')
        if i == 0:
            self.first = self.rest.first
            self.rest = self.rest.rest
        else:
            if self.rest.rest is Link.empty:
                self.rest = Link.empty
            else:
                self.rest.delete_node(i-1)
def remove_duplicates(l):
    uniques= set()
    previous = Link.empty
    while l is not Link.empty:
        if l.first in uniques:
            previous.rest = l.rest
        else:
            uniques.add(l.first)
            previous = l
        l = l.rest
l = Link(1,Link(1, Link(2,Link(2, Link(3, Link(3, Link.empty))))))
remove_duplicates(l)
print(l)
# Here, we assume we don't know len(linked).
def reverse(link):
    reversed = Link.empty
    current = link
    while (current != Link.empty):
        next = current.rest
        current.rest = reversed
        reversed = current
        current = next
    return reversed
def kth_elem(linked, k):
    if k <= 0:
        raise IndexError
    pointer1, pointer2 = linked, linked
    for _ in range(k):
        pointer2 = pointer2.rest
    while pointer2 != Link.empty:
        pointer1, pointer2 = pointer1.rest, pointer2.rest
    return pointer1.first
def delete_node(node):
    if node is Link.empty or node.next is Link.empty:
        raise IndexError('This method cannot delete the last node.')
    node.first = node.rest.first
    node.rest = node.rest.rest
