from arm_controller import ArmController

ac=ArmController()
ac.set_joints([.2,-.5,.3,-.4])
ac.set_joints([-.2,.5,-.3,.4])
ac.set_joints([1,1,1,1])
print(ac.get_pose())
