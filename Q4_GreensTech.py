# Class: GreensTech
# Methods: greens_Omr(id), greens_Adayar(name), greens_Tambaram(address), greens_Velacherry(count)

class GreensTech:
    def greens_Omr(self, id):
        print("Greens OMR ID :", id)

    def greens_Adyar(self, name):
        print("Greens Adyar Name:", name)

    def greens_Tambaram(self, address):
        print("Greens Tambram Address :", address)

    def greens_Velacherry(self, count):
        print("Greens velacherry count :", count)


grns = GreensTech()
grns.greens_Omr("Greens OMR")
grns.greens_Adyar("Head Office")
grns.greens_Tambaram('''No.1, Apparao Colony,
                        Tambaram ,Sanatorium,
                        Near HP Petrol Bunk,
                        Chennai - 600047''')
grns.greens_Velacherry(4)
