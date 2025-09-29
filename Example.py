class MySequence:
    def __len__(self):
        return 3
    def __getitem__(self, index):
        return index * 2

for x in MySequence():  
    print(x)
