# http://eat3d.com/free/maya_python

from pymel.core import *
from xml.dom.minidom import *


startTime = int(playbackOptions(query=True, minTime=True))
stopTime = int(playbackOptions(query=True, maxTime=True))
filePath = "/Users/nick/Desktop/"
fileName = "doc.xml"

openniNames = ["head", "neck", "torso", "l_shoulder", "l_elbow", "l_hand", "r_shoulder", "r_elbow", "r_hand", "l_hip", "l_knee", "l_foot", "r_hip", "r_knee", "r_foot"]
cmuNames = ["Head", "Neck1", "Spine", "LeftArm", "LeftForeArm", "LeftFingerBase", "RightArm", "RightForeArm", "RightFingerBase", "LeftUpLeg", "LeftLeg", "LeftToeBase", "RightUpLeg", "RightLeg", "RightToeBase"]
mobuNames = ["Head", "Neck", "Spine", "LeftArm", "LeftForeArm", "LeftHand", "RightArm", "RightForeArm", "RightHand", "LeftUpLeg", "LeftLeg", "LeftFoot", "RightUpLeg", "RightLeg", "RightFoot"]

# build XML

doc = Document()

root_node = doc.createElement("MotionCapture")
doc.appendChild(root_node)
root_node.setAttribute("width", "640")
root_node.setAttribute("height", "480")
root_node.setAttribute("depth", "200")
root_node.setAttribute("dialogueFile", "none")
root_node.setAttribute("fps", "24")
root_node.setAttribute("numFrames", str(stopTime))

for i in range(startTime, stopTime+1):
	print str(startTime) + " " + str(stopTime)
	currentTime(i)
	frame_node = doc.createElement("MocapFrame")
	root_node.appendChild(frame_node)
	frame_node.setAttribute("index",str(i-1))

	skel_node = doc.createElement("Skeleton")
	frame_node.appendChild(skel_node)
	skel_node.setAttribute("id","0")

	joint_node = doc.createElement("Joints")
	skel_node.appendChild(joint_node)

	target = selected()
	print target

	joints = listRelatives(target[0], ad=True)
	joints.append(target[0])
	print "~~~~~     " + str(joints) + "     ~~~~~"

	for j in range(0,len(joints)):
		try:
			k_node = doc.createElement(str(joints[j]))
			joint_node.appendChild(k_node)

			p = xform(joints[j], q=True, t=True, ws=True)
			k_node.setAttribute("x", str(-1 * p[0]))
			k_node.setAttribute("y", str(-1 * p[1]))
			k_node.setAttribute("z", str(p[2]))
		except:
			print "Couldn't get joint position."

xml_file = open(filePath + fileName, "w")
xml_file.write(doc.toprettyxml())
xml_file.close()

print doc.toprettyxml()