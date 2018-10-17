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

a=np.zeros([4,4])
angl=1.57
import math
a[0,0]=math.cos(angl)
a[0,1]=math.sin(angl)
a[1,0]=-math.sin(angl)
a[1,1]=math.cos(angl)
outpc2 = pcl.PointCloud()
outpc2=pcl.TransformPointCloud(outpc,a)
pcl.save(outpc2,"outfrustum_90deg.pcd")


