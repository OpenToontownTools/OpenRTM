# want-tk 1
# want-directtools 1
# level-editor-hoods TT
level-editor-hoods TT DD DG MM BR DL PA
style-path-prefix /i

#load-display pandadx9
load-display pandagl

framebuffer-multisample 1
multisamples 8

chan-config-sanity-check #f
win-width 1280
win-height 720
fullscreen 0
sync-video #f

# Configrc for running the Robot Toon Manager

want-anim-panel #f

# Use local copy of ttmodels
#model-path /e/Clash/resources/
model-path .
dna-directory .
# Putting this line after ttmodels means models will be read from here first
# model-path     /tt
model-path     $DMODELS

model-path resources

sound-path     .
dna-preload    phase_4/dna/storage.dna
default-model-extension .bam


window-title Toontown

# Custom ObjectTypes for Toontown.
# "barrier" means a vertical wall, with bitmask 0x01
# "floor" means a horizontal floor, with bitmask 0x02
# "camera-collide" means things that the camera should avoid, with bitmask 0x04
egg-object-type-barrier         <Scalar> collide-mask { 0x01 } <Collide> { Polyset descend }
egg-object-type-trigger         <Scalar> collide-mask { 0x01 } <Collide> { Polyset descend intangible }
egg-object-type-sphere          <Scalar> collide-mask { 0x01 } <Collide> { Sphere descend }
egg-object-type-trigger-sphere  <Scalar> collide-mask { 0x01 } <Collide> { Sphere descend intangible }
egg-object-type-floor           <Scalar> collide-mask { 0x02 } <Collide> { Polyset descend }
egg-object-type-camera-collide  <Scalar> collide-mask { 0x04 } <Collide> { Polyset descend }
egg-object-type-camera-collide-sphere  <Scalar> collide-mask { 0x04 } <Collide> { Sphere descend }
egg-object-type-camera-barrier  <Scalar> collide-mask { 0x05 } <Collide> { Polyset descend }
egg-object-type-camera-barrier-sphere  <Scalar> collide-mask { 0x05 } <Collide> { Sphere descend }

# The modelers occasionally put <ObjectType> { model } instead of
# <Model> { 1 }.  Let's be accommodating.
egg-object-type-model           <Model> { 1 }
egg-object-type-dcs             <DCS> { 1 }

# Define a "shadow" object type, so we can render all shadows in their
# own bin and have them not fight with each other (or with other
# transparent geometry).
egg-object-type-shadow          <Scalar> bin { shadow } <Scalar> alpha { blend-no-occlude }
cull-bin shadow 15 unsorted

# The ID of the server that we are compatible with
server-version sv1.0.14


notify-level-chan   error


# This is a MACOS fix, we don't need it as it locks framerates and can cause other issues
tk-main-loop #f

