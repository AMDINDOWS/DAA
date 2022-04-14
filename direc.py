class Animal:
    def __init__(self,name,species,sector):
        self.name=name
        self.species=species
        self.sector=int(sector)
    def g_name(self):
        return self.name
    def g_species(self):
        return self.species
    def g_sector(self):
        return self.sector        
    def __str__(self):
        return f"The details are name={self.name} species={self.species} sector={self.sector}"

class Jungledirectory:

    def __init__(self,animallst):
        self.__animallst=animallst

    def search(self,k_name):
        out_lst=[]
        for i in self.__animallst:
            if(k_name in i.g_name()):
                out_lst.append(i)
            self.display(out_lst)
            return out_lst
    def display(self,out_lst):
        print("Results")
        for i in out_lst:
            print (f"{i.g_name()} {i.g_species()} {i.g_sector()}")          

an1=Animal("Lion","Cats",1)
an2=Animal("Pegion","Avian",2)
an3=Animal("Salamander","Amphibian",4)

am_lst=[an1,an2,an3]

jun_dir1=Jungledirectory(am_lst)

jun_dir1.search("Pegion")
#print(an1)