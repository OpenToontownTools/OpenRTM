#version 130
uniform sampler2D p3d_Texture0;
uniform vec4 p3d_ColorScale;
in vec4 vColor;
in vec2 texcoord;
out vec4 color;

// TODO: Make these props actually react to the fog
uniform struct p3d_FogParameters {
  vec4 color;
  float density;
  float start;
  float end;
  float scale; // 1.0 / (end - start)
} p3d_Fog;

void main() {
  color = p3d_ColorScale * texture(p3d_Texture0, texcoord) * vColor;
}