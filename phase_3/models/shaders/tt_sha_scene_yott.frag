// Corporate Clash Ye Olde Toontown Post Process
#version 430
uniform sampler2D p3d_Texture0;
uniform float osg_FrameTime;
in vec2 texcoord;
out vec4 color;

vec3 adjustSaturation(vec3 rgb, float adjustment)
{
    const vec3 W = vec3(0.2125, 0.7154, 0.0721);
    vec3 intensity = vec3(dot(rgb, W));
    return mix(intensity, rgb, adjustment);
}

void main() {
	color = texture(p3d_Texture0, texcoord);
	float lum = dot(color.rgb, vec3(0.299, 0.587, 0.114));
	float strength = 16.0;
        
	//color = vec4(lum, lum, lum, 1.0);
	
	color = vec4(adjustSaturation(color.rgb, .4), 1.0);
	
	
	
	float noise = fract(10000 * sin((gl_FragCoord.x + gl_FragCoord.y * osg_FrameTime) * 3.14/180));
	color.rgb += 0.1*noise;
}