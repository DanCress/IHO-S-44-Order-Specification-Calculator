from dictionary_module import EO, SO, OA, OB, OT #imports from the dict.py the properties of each order

mindepth = float(input("Input minimum site depth (m): ")) #user specifies minimum estimated site depth
maxdepth = float(input("Input maxmimum site depth (m): ")) #user specifies maximum estimated site depth

class Order:
    def __init__ (self, a, b, perdep, Area_Description, Depth_THU, Depth_TVU, Feature_Detection, Feature_Search, Bathymetric_Coverage): #[1] class variables
        self.a = a #establishing the class variables to be fed from the order instance variables (see [2])
        self.b = b
        self.perdep = perdep
        self.Area_Description = Area_Description
        self.Depth_THU = Depth_THU
        self.Depth_TVU = Depth_TVU
        self.Feature_Detection = Feature_Detection
        self.Feature_Search = Feature_Search
        self.Bathymetric_Coverage = Bathymetric_Coverage
    
    def AreaDescription(self): #prints area description from dictionary based on the instance (see [2])
        print(" \n=== Criteria calculated below ===\n")
        print(f"{self.Area_Description}")
    
    def DepthTHU(self): #calculates max depth THU from the input depths. if == 1, the value is simply as passed from the below instance variables (see [2]), otherwise it is some percentage of depth according to S-44
        if {self.perdep} != 1:
            THU_min = round(self.Depth_THU + (mindepth * (self.perdep - 1)), 4)
            THU_max = round(self.Depth_THU + (maxdepth * (self.perdep - 1)), 4)
            print("Total Horizontal Uncertainty maximum @ ", mindepth, "m depth is:", THU_min, "m")
            print("Total Horizontal Uncertainty maximum @ ", maxdepth, "m depth is:", THU_max, "m")
        else:
            print(f"Total Horizontal Uncertainity maximum is: {self.Depth_THU} m")
            
    def DepthTVU(self): #calculates max depth TVU from the input depths
        TVU_min = round(((self.a)**2+(self.b * mindepth)**2)**0.5, 4)
        TVU_max = round(((self.a)**2+(self.b * maxdepth)**2)**0.5, 4)     
        print("Total Vertical Uncertainity maximum @ ", mindepth, "m depth is: ", TVU_min, "m")
        print("Total Vertical Uncertainity maximum @ ", maxdepth, "m depth is: ", TVU_max, "m")
        
    def FeatureDetection(self): #prints feature description from the dictionary. if Order 1a, an additional print for the + percentage in S44 is given
        print(f"Feature Detection criteria is: {self.Feature_Detection}")
        if classinput == "1A":
            print("O1A: 10% of ", mindepth, "m depth (minimum) is: ", round(mindepth * 0.10, 3), "m")
            print("O1A: 10% of ", maxdepth, " m depth (maximum) is: ", round(maxdepth * 0.10, 3), "m")
        
    def FeatureSearch(self): #prints feature search criteria from the dictionary based on the instance (see [2])
        print(f"Feature Search criteria is: {self.Feature_Search}")
        
    def BathymetricCoverage(self): #prints bathymetric coverage from the dictionary based on the instance (see [2])
        print(f"Bathymetric Coverage criteria is: {self.Bathymetric_Coverage}")
        
classinput = input("Select Order (Type EO, SO, 1A, 1B, or 2) (Note: O is the LETTER O):") #user states desired order version

#instance variable format for below is: a, b, perdep. AreaDesc, Depth_THU(Percentage), Depth_TVU, Feature_Detec, Feature_Search, Bathymetric Coverage
#dictionary reference format is AD, FD, FS, BC

if classinput == "EO": #if exclusive order, etc...
    order = Order(0.15, 0.0075, 1, EO["AD"], 1, 0, EO["FD"], EO["FS"], EO["BC"]) #define the class variables past self as... (see [1]) [2] directs here
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage() #execute these functions within the class object if order == this
elif classinput == "SO": #if special order... you get the idea
    order = Order(0.25, 0.0075, 1, SO["AD"], 2, 0, SO["FD"], SO["FS"], SO["BC"])
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "1A":
    order = Order(0.5, 0.013, 1.05, OA["AD"], 5, 0, OA["FD"], OA["FS"], OA["BC"])
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "1B":
    order = Order(0.5, 0.013, 1.05, OB["AD"], 5, 0, OB["FD"], OB["FS"], OB["BC"])
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "2":
    order = Order(1, 0.023, 1.10, OT["AD"], 20, 0, OT["FD"], OT["FS"], OT["BC"])
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
else:
    print("Wrong input. Type either EO, SO, 1A, 1B, or 2") #error check in case anything but the above instance strings are input by the user in classinput
    pass

input("\nComplete! Press any key to exit...")

