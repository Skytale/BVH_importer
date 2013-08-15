# http://eat3d.com/free/maya_python

#from pymel.core import *
#from xml.dom.minidom import *


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

	selection = ls(sl = True)
	print selection

	for object in selection:
		try:
			kids = listRelatives(ls(selection=True), children=True, type="joint", allDescendents=True)
			for k in kids:
				print k
				k_node = doc.createElement(str(k))
				joint_node.appendChild(k_node)

				p = xform(k, q=True, t=True, ws=True)
				k_node.setAttribute("x", str(-1 * p[0]))
				k_node.setAttribute("y", str(-1 * p[1]))
				k_node.setAttribute("z", str(p[2]))
		except:
			print "No child joints."
		print object
		
		object_node = doc.createElement(str(object))
		joint_node.appendChild(object_node)

		p = xform(k, q=True, t=True, ws=True)
		object_node.setAttribute("x", str(-1 * p[0]))
		object_node.setAttribute("y", str(-1 * p[1]))
		object_node.setAttribute("z", str(p[2]))

xml_file = open(filePath + fileName, "w")
xml_file.write(doc.toprettyxml())
xml_file.close()

print doc.toprettyxml()