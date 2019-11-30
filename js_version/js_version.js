class Properties{
  constructor(props){
    this.props = props;
  }
  setProps(props){
    Object.assign(this.props,props);
  }
}

class CameraObject extends Properties{
  constructor(props){
    super(props);
  }
}

class SpaceElement extends Properties{
  constructor(props){
    super(props);
  }
  get position(){
    return props.position;
  }
  
  set position(position){
    setProps({position: position,});
  }
  
  get momentum(){
    return props.momentum;
  }
  
  set momentum(momentum){
    setProps({momentum: momentum,});
  }
  
  get color(){
    return props.color;
  }
  
  set color(color){
     setProps({color: color,});
  }
  
  get stroke_color(){
    return props.stroke_color;
  }
  
  set stroke_color(stroke_color){
     setProps({stroke_color: stroke_color,});
  }
  
}

class Dot extends SpaceElement{
  constructor(props){
    super(props);
    if(typeof props.stroke_color === 'undefined'){
      this.setProps({stroke_color: [240,240,240,],});
    }
  }
  
  update(){
    
  }
    
  draw(){
    push();
    try{
    stroke(this.props.stroke_color[0],this.props.stroke_color[1],this.props.stroke_color[2]);
    }catch(error){}
    try{
    fill(this.props.color[0],this.props.color[1],this.props.color[2]);
    }catch(error){}
    try{
    translate(this.props.position[0],this.props.position[1],this.props.position[2]);
    }catch(error){}
    try{
    sphere(25);
    }catch(error){
    
    }
    pop();
  }
}

class DotGroup extends SpaceElement{
  constructor(props){
    super(props);
    if(typeof props.dots === 'undefined'){
      this.setProps({dots: [],});
    }
  }
  
  update(){
    this.props.dots.map((dot,index) => (dot.update()));
  }
  
  draw(){
    this.props.dots.map((dot,index) => (dot.draw()));
  }
  
  get dots(){
    return this.props.dots;
  }
  set dots(dots){
     setProps(dots);
  }
  
  addDot(dot){
    this.dots.push(dot);
  }
  
}

function setup() {
  createCanvas(710, 400, WEBGL);
}
function draw() {
  background(0,52,255);
  (new DotGroup({dots: [new Dot({position: [10,10,10,],}), new Dot({position: [40,0,10,],}),],})).draw();
  //drag to move the world.
  orbitControl();
}
