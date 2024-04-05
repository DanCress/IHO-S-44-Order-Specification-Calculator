from dictionary_module import EO, SO, OA, OB, OT

mindepth = float(input("Input minimum site depth (m): "))
maxdepth = float(input("Input maxmimum site depth (m): "))

class Order:
    def __init__ (self, a, b, perdep, Area_Description, Depth_THU, Depth_TVU, Feature_Detection, Feature_Search, Bathymetric_Coverage):
        self.a = a
        self.b = b
        self.perdep = perdep
        self.Area_Description = Area_Description
        self.Depth_THU = Depth_THU
        self.Depth_TVU = Depth_TVU
        self.Feature_Detection = Feature_Detection
        self.Feature_Search = Feature_Search
        self.Bathymetric_Coverage = Bathymetric_Coverage
    
    def AreaDescription(self):
        print(" \n=== Criteria calculated below ===\n")
        print(f"{self.Area_Description}")
    
    def DepthTHU(self):
        if {self.perdep} != 1:
            THU_min = round(self.Depth_THU + (mindepth * (self.perdep - 1)), 4)
            THU_max = round(self.Depth_THU + (maxdepth * (self.perdep - 1)), 4)
            print("Total Horizontal Uncertainty maximum @ ", mindepth, "m depth is:", THU_min, "m")
            print("Total Horizontal Uncertainty maximum @ ", maxdepth, "m depth is:", THU_max, "m")
        else:
            print(f"Total Horizontal Uncertainity maximum is: {self.Depth_THU} m")
            
    def DepthTVU(self):
        TVU_min = round(((self.a)**2+(self.b * mindepth)**2)**0.5, 4)
        TVU_max = round(((self.a)**2+(self.b * maxdepth)**2)**0.5, 4)     
        print("Total Vertical Uncertainity maximum @ ", mindepth, "m depth is: ", TVU_min, "m")
        print("Total Vertical Uncertainity maximum @ ", maxdepth, "m depth is: ", TVU_max, "m")
        30
    def FeatureDetection(self):
        print(f"Feature Detection criteria is: {self.Feature_Detection}")
        if classinput == "1A":
            print("O1A: 10% of ", mindepth, "m depth (minimum) is: ", round(mindepth * 0.10, 3), "m")
            print("O1A: 10% of ", maxdepth, " m depth (maximum) is: ", round(maxdepth * 0.10, 3), "m")
        
    def FeatureSearch(self):
        print(f"Feature Search criteria is: {self.Feature_Search}")
        
    def BathymetricCoverage(self):
        print(f"Bathymetric Coverage criteria is: {self.Bathymetric_Coverage}")
        
classinput = input("Select Order (Accepts EO, SO, 1A, 1B, 2):")

#a, b, perdep. AreaDesc, Depth_THU(Percentage), Depth_TVU, Feature_Detec, Feature_Search, Bathymetric Coverage

if classinput == "EO": #AD, FD, FS, BC
    order = Order(0.15, 0.0075, 1, EO["AD"], 1, 0, EO["FD"], EO["FS"], EO["BC"])
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "SO":
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
    print("Wrong input. Type either EO, SO, 1A, 1B, 2")
    pass



