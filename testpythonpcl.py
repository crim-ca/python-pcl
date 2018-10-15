import pcl
import numpy as np

pc=pcl.load("table.pcd")
fc=pcl.FrustumCulling(pc)
fc.SetHorizontalFOV(130)
fc.SetVerticalFOV(60)
fc.SetNearPlaneDistance(0)
fc.SetFarPlaneDistance(1)
campose=np.array([[1, 0, 0, 0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float)
fc.SetCameraPose(campose)
outpc=fc.filter()
pcl.save(outpc,"outfrustum.pcd")


