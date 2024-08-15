import React from 'react';
import Slider from "react-slick";
interface sliderProps  {
  page: number,
  dot: boolean,
}

function Slider(props: sliderProps): React.JSX.Element {
  const setting = {
    dots: props.dot,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
  }

  return (
    <div>

    </div>
  );
}

export default Slider;
