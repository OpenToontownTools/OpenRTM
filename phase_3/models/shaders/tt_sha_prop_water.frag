#version 130
uniform vec4 p3d_ColorScale;
uniform sampler2D p3d_Texture0;

in vec2 texcoord;


void main() {
  //gl_FragColor = p3d_ColorScale * texture(p3d_Texture0, texcoord) * vec4(1.0, 1.0, 1.0, 0.2);
  gl_FragColor = texture(p3d_Texture0, texcoord) * vec4(1.0, 1.0, 1.0, 0.2);
}