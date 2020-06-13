#version 430
uniform sampler2D p3d_Texture0;
in vec2 texcoord;
out vec4 color;
void main() {
	color = texture(p3d_Texture0, texcoord);  
}