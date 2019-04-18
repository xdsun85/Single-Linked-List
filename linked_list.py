# coding:utf-8

class Node(object):
    '''
    elem: 节点保存的数据
    next: 保存下一个节点对象
    '''
    def __init__(self, init_elem=-1, pnext=None):
        self.elem = init_elem
        self.next = pnext

class SingleLinkedList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return not self._head

    def append(self, elem):
        node = Node(elem)
        if not self._head:      # 若链表为空，head指向新节点
            self._head = node
        else:                           # 否则，循环到链表末尾，指向新节点
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def add(self, elem):  # 从头加
        node = Node(elem)
        node.next = self._head
        self._head = node

    def traverse(self):
        cur = self._head
        L = []
        while cur:
            L.append(cur.elem)
            cur = cur.next
        print(L)

    def len(self):
        cur = self._head
        i = 0
        while cur:
            cur = cur.next
            i += 1
        return i

    def is_in(self, elem):
        cur = self._head
        while cur:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False

    def count(self, elem):
        cur = self._head
        cnt = 0
        while cur:
            if cur.elem == elem:
                cnt += 1
            cur = cur.next
        return cnt

    def index(self, elem):
        cur = self._head
        i = 0
        while cur:
            if cur.elem == elem:
                return i
            cur = cur.next
            i += 1
        return 'Not Found!'

    def indices(self, elem):
        cur = self._head
        i = 0
        L = []
        while cur:
            if cur.elem == elem:
                L.append(i)
            cur = cur.next
            i += 1
        return L

    # 获得指定位置节点的值
    def get_value(self, index):
        if not self._head:
            return 'Empty List!'
        elif index < 0:
            return 'List index (%s) out of range!' % index
        else:
            cur = self._head
            for i in range(index):
                if cur.next:
                    cur = cur.next
                else:
                    return 'List index (%s) out of range!' % index
            return cur.elem

    # 有了len()之后，get_value的另一种方法。index允许为负值
    # 但调了len(), Time Complexity就变O(2n)了
    def get_value_1(self, index):
        n = self.len()
        if not self._head:
            return 'Empty List!'
        elif index < -n or index >= n:
            return 'List index (%s) out of range!' % index
        else:
            if index < 0:
                index += n
            cur = self._head
            cnt = 0
            while cnt < index:
                cur = cur.next
                cnt += 1
            return cur.elem

    # 更新指定位置节点的值
    def update(self, index, value):
        if not self._head:
            print('Empty List!')
        elif index < 0:
            print('List index (%s) out of range!' % index)
        else:
            cur = self._head
            for i in range(index):
                if cur.next:
                    cur = cur.next
                else:
                    print('List index (%s) out of range!' % index)
                    return
            cur.elem = value

    # 有了len()之后，update的另一种方法。index允许为负值
    # 但调了len(), Time Complexity就变O(2n)了
    def update_1(self, index, value):
        n = self.len()
        if not self._head:
            print('Empty List!')
        elif index < -n or index >= n:
            print('List index (%s) out of range!' % index)
        else:
            if index < 0:
                index += n
            cur = self._head
            cnt = 0
            while cnt < index:
                cur = cur.next
                cnt += 1
            cur.elem = value

    # 删元素，有多个只删第一个
    def remove(self, elem):
        hasRemoved = False
        if not self._head:
            print('Empty List!')
        else:
            if self._head.elem == elem:     # 首元素
                self._head = self._head.next
                hasRemoved = True
            else:                                           # 非首元素
                prev = self._head        # prev将指向待删节点的前一个位置
                while prev.next and hasRemoved is False:
                    if prev.next.elem == elem:
                        prev.next = prev.next.next      # 删除prev指向节点的下一个
                        hasRemoved = True
                    else:
                        prev = prev.next

            if hasRemoved:
                print('The 1st \'%s\' was removed.' % elem)
            else:
                print('Not Found!')

    # 删除所有值为elem的节点
    def remove_all(self, elem):
        hasRemoved = False
        cnt = 0
        if not self._head:
            print('Empty List!')
        else:
            # 目标元素位于首部，删之
            while self._head and self._head.elem == elem:
                self._head = self._head.next
                hasRemoved = True
                cnt += 1
            # 删完首部的目标元素，继续寻而删之
            if self._head:
                prev = self._head        # prev将指向待删节点的前一个位置
                while prev.next:
                    if prev.next.elem == elem:
                        prev.next = prev.next.next
                        hasRemoved = True
                        cnt += 1
                        continue
                    else:
                        prev = prev.next

            if hasRemoved is True:
                print('%s \'%s\'(s) were removed.' % (cnt, elem))
            else:
                print('Not Found!')

    # 删index
    def delete(self, index):
        if not self._head:
            print('Empty List!')
        elif index < 0:
            print('List index (%s) out of range!' % index)
        else:
            if 0 == index:
                self._head = self._head.next
                print('The 0th element was removed.')
            else:
                prev = self._head    # prev将指向位置index-1的节点
                if not prev.next:
                    # 若index不为0, 节点数必须多于1
                    print('List index (%s) out of range!' % index)
                    return
                # 用一般for循环：
                for i in range(index - 1):
                    if prev.next.next:
                        prev = prev.next
                    else:
                        print('List index (%s) out of range!' % index)
                        return
                # 此时prev已指向了index-1
                prev.next = prev.next.next  # 删之
                print('The %s. element was removed.' % index)
                # 用for-else语句：
                # for i in range(index - 1):
                #     if not prev.next.next:
                #         print('List index (%s) out of range!' % index)
                #         break
                #     else:
                #         prev = prev.next
                # # 此时prev已指向了index-1
                # else:
                #     # for循环未被break中断(未超出范围)，执行删除操作
                #     prev.next = prev.next.next
                #     print('The %s. element was removed.' % index)

    # 有了len()之后，删index的另一种方法。index允许为负值
    # 但调了len(), Time Complexity就变O(2n)了
    def delete_1(self, index):
        n = self.len()
        if not self._head:
            print('Empty List!')
        elif index < -n or index >= n:
            print('List index (%s) out of range!' % index)
        else:
            if index < 0:
                index += n
            if 0 == index:
                self._head = self._head.next
                print('The 0th element was removed.')
            else:
                prev = self._head
                cnt = 1
                while cnt < index:
                    prev = prev.next
                    cnt += 1
                # 移到了，prev指向了index-1. 删之
                prev.next = prev.next.next
                print('The %s. element was removed.' % index)

    def clear(self):
        self._head = None

    # 浅拷贝，只共享指针
    def copy(self):
        new_linked_list = SingleLinkedList()
        new_linked_list._head = self._head
        return new_linked_list

    def extend(self, list_b):
        if not self._head:       # 若自己是空链表
            self._head = list_b._head
        else:
            cur_a = self._head
            while cur_a.next:
                cur_a = cur_a.next
            cur_a.next = list_b._head
        return self._head

    # 统计元素分布
    def histogram(self):
        cur = self._head
        dict = {}
        while cur:
            dict[cur.elem] = dict.setdefault(cur.elem, 0) + 1
            cur = cur.next
        print(dict)

    # 去重
    def distinct(self):
        if self._head and self._head.next:  # 节点数多于1才需要去重
            prev = self._head
            L = [self._head.elem]
            while prev.next:
                if prev.next.elem not in L:
                    L.append(prev.next.elem)
                    prev = prev.next
                else:
                    prev.next = prev.next.next  # 删掉prev指向的节点的下一个

    # 指定位置前插入节点
    def insert(self, pos, elem):
        if not self._head or pos <= 0:
            # 空链表 或 插入位置小于等于0
            self.add(elem)
        else:
            prev = self._head        # prev将指向位置pos-1的节点
            # 用一般for循环：
            for i in range(pos - 1):
                if prev.next:
                    prev = prev.next
                else:
                    self.append(elem)
                    return
            node = Node(elem)
            node.next = prev.next
            prev.next = node
            # 用for-else语句：
            # for i in range(pos - 1):
            #     if not prev.next:
            #         self.append(elem)
            #         break
            #     else:
            #         prev = prev.next
            # else:
            #     # for循环未被break中断(未超出范围)，执行删除操作
            #     node = Node(elem)
            #     node.next = prev.next
            #     prev.next = node

    # 有了len()之后，insert的另一种方法。index允许为负值
    # 但调了len(), Time Complexity就变O(2n)了
    def insert_1(self, pos, elem):
        n = self.len()
        if not self._head or pos <= -n or 0 == pos:
            # 空链表 或 插入位置小于等于-n或等于0
            self.add(elem)
        elif pos >= n:
            # 位置超出末位
            self.append(elem)
        else:
            if pos < 0:
                pos += n
            node = Node(elem)
            prev = self._head        # prev将指向位置pos-1的节点
            cnt = 1
            while cnt < pos:
                prev = prev.next
                cnt += 1
            node.next = prev.next
            prev.next = node

    # 仿pop：返回第index个值，并将之从链表中删除；
    # 若index缺省，则返回链表尾部的值，并删之
    def pop(self, index=-1):
        if not self._head:
            print('Empty List!')
        elif index < -1:
            print('List index (%s) out of range!' % index)
        else:
            if 0 == index:
                # 弹第一个
                res = self._head.elem
                self._head = self._head.next
                return res
            elif -1 == index:
                # 弹最后一个
                # 其实无需区别操作最后一个和中间节点，只是index为-1时for循环终止条件不好写
                if not self._head.next:
                    # 只有一个节点
                    res = self._head.elem
                    self._head = None
                    return res
                else:
                    # 节点数多于1
                    prev = self._head
                    while prev.next.next:
                        prev = prev.next
                    res = prev.next.elem
                    prev.next = None
                    return res
            else:
                # 弹中间元素
                prev = self._head        # prev将指向位置index-1的节点
                if not prev.next:
                    # 若index不为0或-1, 节点数必须多于1
                    print('List index (%s) out of range!' % index)
                    return
                # 用一般for循环：
                for i in range(index - 1):
                    if prev.next.next:
                        prev = prev.next
                    else:
                        print('List index (%s) out of range!' % index)
                        return
                # 此时prev已指向了待弹元素的前一位
                res = prev.next.elem
                prev.next = prev.next.next  # 删之
                return res
                # 用for-else语句：
                # for i in range(index - 1):
                #     if not prev.next.next:
                #         print('List index (%s) out of range!' % index)
                #         break
                #     else:
                #         prev = prev.next
                # # 此时prev已指向了待弹元素的前一位
                # else:
                #     # for循环未被break中断(未超出范围)，执行删除操作
                #     res = prev.next.elem
                #     prev.next = prev.next.next
                #     return res

    # 有了len()之后，pop的另一种方法。index允许为-1以外的负值
    # 但调了len(), Time Complexity就变O(2n)了
    def pop_1(self, index=-1):
        n = self.len()
        if not self._head:
            print('Empty List!')
        elif index < -n or index >= n:
            print('List index (%s) out of range!' % index)
        else:
            if index < 0:
                index += n
            if 0 == index:
                # 弹第一个
                res = self._head.elem
                self._head = self._head.next
                return res
            else:
                # 弹中间元素或末尾元素
                prev = self._head        # prev将指向位置index-1的节点
                cnt = 1
                while cnt < index:
                    prev = prev.next
                    cnt += 1
                # 此时prev已指向了待弹元素的前一位
                res = prev.next.elem
                prev.next = prev.next.next  # 删之
                return res

    # 百分位数。0.25: 第一四分位数；0.5: 中位数；0.75: 第三四分位数
    def percentile(self, percent):
        if not self._head:
            return 'Empty List!'
        if percent < 0 or percent > 1:
            return 'The Percent must be between 0 and 1!'
        cur = self._head
        L = []
        i = 0
        while cur:
            L.append(cur.elem)
            cur = cur.next
            i += 1
        L.sort()        # 为避免改变原链表顺序，不应对原链表排序
        if 1 == percent:    # percent为1时，L[int(percent * i)]会越界
            return L[-1]
        else:
            return L[int(percent * i)]

    def swap(self, i, j):
        t = self.get_value(j)
        self.update(j, self.get_value(i))
        self.update(i, t)

    def bubble_sort(self):
        for i in range(self.len())[::-1]:
            for j in range(i):
                if self.get_value(j) > self.get_value(j + 1):
                    self.swap(j, j + 1)

    def insertion_sort(self):
        for i in range(1, self.len()):
            # 把[i]插入已排好的[:i]中
            k = i
            for j in range(i - 1, -1, -1):      # 从i-1到0
                if self.get_value(k) < self.get_value(j):
                    self.swap(k, j)
                    k -= 1
                    # 如发生交换，指针k因为要始终指向待插元素[i], 也得一路前移

    def quick_sort(self, left, right):
        i = left
        j = right

        if i >= j:
            return

        key = self.get_value(i)
        while i < j:
            while i < j and self.get_value(j) >= key:
                j -= 1
            self.swap(i, j)
            while i < j and self.get_value(i) <= key:
                i += 1
            self.swap(j, i)
        self.update(i, key)

        self.quick_sort(left, i - 1)
        self.quick_sort(j + 1, right)

    # 返回链表中点的指针
    def get_mid(self, head):
        if not head:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None  # 从中间截断链表

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        self._head = self.merge(left, right)
        '''
        要将原链表的头指针(self._head)改为排序后链表的头指针(使其指
        向最小元素)。链表merge sort的本质是改变一系列指针的指向(这
        点和quick sort互换一系列节点的动作不同，由于quick sort未动指
        针，所以原链表的头指针不用改)。如果每次merge后头指针还指
        向原始头元素，经过一次指针重构后，头指针就可能指向中部的
        某元素，最后traverse就可能只打印出原始头元素及其排序后的后
        续元素。故而需要将链表头指针始终指向排序后的首元素，并返
        回这个新的头指针。
        '''
        return self._head

    def merge(self, p, q):
        tmp = Node(-1)
        h = tmp
        while p and q:
            if p.elem < q.elem:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return tmp.next

    def reverse(self):
        if self._head and self._head.next:    # 节点数多于1才有反转的意义
            cur = self._head
            newHead = None
            while cur:
                # post关键了！如果直接修改cur.next, 没有了指向下一节点的引用，链表就断了
                post = cur.next
                cur.next = newHead
                newHead = cur
                cur = post
            self._head = newHead

    # 用递归
    def reverse_1(self, head):
        if not head or not head.next:    # 节点数多于1才有反转的意义
            return head
        newHead = self.reverse_1(head.next)
        head.next.next = head
        head.next = None

        self._head = newHead
        return self._head

    # 检测是否有环
    # 返回一个Tuple, [0]: True / False; [1]: 环的入口；[2]: 环长
    def has_circle(self):
        if not self._head:
            print('Empty List!')
            return False, -1, 0
        fast = slow = self._head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 快慢指针相遇，有环。下面找环的入口
                slow = self._head
                entr = 0
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    entr += 1
                # slow停下，fast再走一圈，数出环长
                fast = fast.next
                c = 1
                while slow != fast:
                    fast = fast.next
                    c += 1
                return True, entr, c
        return False, -1, 0

    def break_circle(self):
        circle_info = self.has_circle()
        if circle_info[0]:      # 有环
            cur = self._head
            i = 0
            while i < circle_info[1] + circle_info[2] - 1:
                cur = cur.next
                i += 1
            # 此时cur指向“末节点”
            cur.next = None
            print('Circle Broken.')
        else:
            print('No Circle!')

if __name__ == '__main__':

    myLinkedList = SingleLinkedList()
    myLinkedList.append(1)
    print('Is empty: ', myLinkedList.is_empty())
    myLinkedList.add(2)
    myLinkedList.append(2)
    myLinkedList.add(1)
    myLinkedList.append(3)
    myLinkedList.append(6)
    myLinkedList.traverse()

    print('Length:', myLinkedList.len())
    print('Is 3 in the list: ', myLinkedList.is_in(3))
    print('The num of 1: ', myLinkedList.count(1))
    print('The index of 2: ', myLinkedList.index(2))
    print('The indices of 2s: ', myLinkedList.indices(2))
    print('The 1. elem: ', myLinkedList.get_value(1))
    print('The -1. elem: ', myLinkedList.get_value_1(-1))
    myLinkedList.update(1, 1)
    myLinkedList.update_1(-1, 3)
    myLinkedList.traverse()

    myLinkedList.remove(1)
    myLinkedList.traverse()

    myLinkedList.remove_all(1)
    myLinkedList.traverse()

    myLinkedList.delete(1)
    myLinkedList.traverse()

    myLinkedList.delete_1(-1)
    myLinkedList.traverse()

    myLinkedList.clear()
    print('Is empty: ', myLinkedList.is_empty())

    aList = SingleLinkedList()
    aList.append(1)
    aList.append(3)
    myLinkedList = aList.copy()
    myLinkedList.traverse()

    bList = SingleLinkedList()
    bList.append(1)
    bList.append(4)
    myLinkedList.extend(bList)
    myLinkedList.traverse()

    myLinkedList.histogram()
    myLinkedList.distinct()
    myLinkedList.traverse()

    myLinkedList.insert(0, 0)
    myLinkedList.insert_1(-2, 2)
    myLinkedList.traverse()

    print('The 1st quartile: ', myLinkedList.percentile(0.25))
    print('The 3th quartile: ', myLinkedList.percentile(0.75))

    print('The popped elem: ', myLinkedList.pop(1))
    print('The popped elem: ', myLinkedList.pop())
    print('The popped elem: ', myLinkedList.pop_1())
    print('The popped elem: ', myLinkedList.pop_1(-1))
    myLinkedList.traverse()

    myLinkedList.add(1)
    myLinkedList.add(2)
    myLinkedList.add(3)
    myLinkedList.bubble_sort()
    myLinkedList.traverse()

    myLinkedList.reverse()
    myLinkedList.insertion_sort()
    myLinkedList.traverse()

    myLinkedList.reverse_1(myLinkedList._head)
    myLinkedList.quick_sort(0, myLinkedList.len() - 1)
    myLinkedList.traverse()

    myLinkedList.reverse_1(myLinkedList._head)
    myLinkedList.merge_sort(myLinkedList._head)
    myLinkedList.traverse()

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    cList = SingleLinkedList()
    cList._head = node0
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2

    print(cList.has_circle())
    cList.break_circle()
    cList.traverse()
