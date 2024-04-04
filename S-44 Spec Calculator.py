#Dictonary:

EO = {
      "AD": "Areas where there is strict minimum underkeel clearance and manoeuvrability criteria"
      }

SO = {
      "AD": "Areas where underkeel clearance is critical."
      }

OA = {
      "AD": "Areas where underkeel clearance is considered not to be critical but features of concern to surface shipping may exist."
      }

OB = {
      "AD": "Areas where underkeel clearance is not considered to be an issue for the type of surface shipping expected to transit the area."
      }

OT = {
      "AD": "Areas where a general description of the seafloor is considered adequate."
      }

depth = 40

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
        print(f"{self.Area_Description}")
    
    def DepthTHU(self):
        if {self.perdep} != 1:
            THU = self.Depth_THU + (self.Depth_THU * (self.perdep - 1))
            print("Total Horizontal Uncertainty is:", THU, " m")
        else:
            print(f"Total Horizontal Uncertainity is: {self.Depth_THU} m")
            
    def DepthTVU(self):
        print(f"{self.Depth_TVU}")
        
    def FeatureDetection(self):
        print(f"{self.Feature_Detection}")
        
    def FeatureSearch(self):
        print(f"{self.Feature_Search}")
        
    def BathymetricCoverage(self):
        print(f"{self.Bathymetric_Coverage}")
        
classinput = input("Select Order:")

#a, b, perdep

if classinput == "EO":
    order = Order(0.15, 0.0075, 1, EO["AD"], 1, 6, 7, 8, 9)
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "SO":
    order = Order(0.25, 0.0075, 1, SO["AD"], 2, 6, 7, 8, 9)
    order.AreaDescription(), order.Depth_THU(), order.Depth_TVU(), order.Feature_Detection(), order.Feature_Search(), order.Bathymetric_Coverage()
elif classinput == "1A":
    order = Order(0.5, 0.013, 1.05, OA["AD"], 5, 6, 7, 8, 9)
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "1B":
    order = Order(0.5, 0.013, 1.05, OB["AD"], 5, 6, 7, 8, 9)
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
elif classinput == "2":
    order = Order(1, 0.023, 1.10, OT["AD"], 20, 6, 7, 8, 9)
    order.AreaDescription(), order.DepthTHU(), order.DepthTVU(), order.FeatureDetection(), order.FeatureSearch(), order.BathymetricCoverage()
else:
    print("Wrong input")
    pass



