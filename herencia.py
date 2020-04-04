class Computer:
    def __init__(self, cpu, gpu, ram, rom, motherboard):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.rom = rom
        self.motherboard = motherboard
    
    def iniciar(self):
        if (self.cpu and self.gpu) and ((self.ram and self.rom) and (self.motherboard)):
            print('Tienes una PC')
    
class SmartPhone(Computer):
    def __init__(self, cpu, gpu, ram, rom, motherboard,batery=None, screen=None):
        super().__init__(cpu, gpu, ram, rom, motherboard)
        self.batery = batery
        self.screen = screen

    def iniciar(self):
        if self.batery and self.screen:
            print('Tienes un SmatPhone')
        else:
            print('Tienes una Pc')
    

if __name__ == "__main__":
    pc = Computer('intel', 'nvidia', 4, 500, 'Asus')
    phone = SmartPhone('A12', 'MaliG610', 6, 128, 'apple', 500, 5.9)
    pc.iniciar()
    phone.iniciar()
    
