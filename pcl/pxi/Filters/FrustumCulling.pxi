# -*- coding: utf-8 -*-
from libcpp.vector cimport vector
from libcpp cimport bool
x
cimport pcl_defs as cpp
cimport pcl_filters as pclfil

from boost_shared_ptr cimport shared_ptr

cdef class FrustumCulling:
    """
    Must be constructed from the reference point cloud, which is copied, 
    so changed to pc are not reflected in FrustumCulling(pc).
    """
    cdef pclfil.FrustumCulling_t *me

    def __cinit__(self, PointCloud pc not None):
        self.me = new pclfil.FrustumCulling_t()
        (<cpp.PCLBase_t*>self.me).setInputCloud (pc.thisptr_shared)

    def __dealloc__(self):
        del self.me

    def set_InputCloud(self, PointCloud pc not None):
        (<cpp.PCLBase_t*>self.me).setInputCloud (pc.thisptr_shared)

    def filter(self):
        cdef PointCloud pc = PointCloud()
        self.me.c_filter(pc.thisptr()[0])
#        print("filter: pc size = " + str(pc.size))
        return pc


