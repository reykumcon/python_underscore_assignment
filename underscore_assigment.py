class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
    def filter(self, iterable, callback):
        filter_iterable = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                filter_iterable.append(iterable[i])
        return filter_iterable

    def reject(self, iterable, callback):
        reject_iterable = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                reject_iterable.append(iterable[i])
        return reject_iterable

_ = Underscore()
print(_.map([1,2,3], lambda num: num*2))
print(_.find([1,2,3,4,5,6], lambda x: x>4))
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0))
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0))