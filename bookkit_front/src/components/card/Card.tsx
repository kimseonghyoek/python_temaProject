import React from 'react';
import styled from "styled-components";

const StyledCard = styled.div`
  width: 90%;
  background-color: #df2e7f;
  margin: 1rem;
  
  .wrap_contents {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  
    .wrap_img {
      padding: 2rem;
    }
  }
`;
// 크롤링한 데이터: 순서, 책 이름, 작가, 소개글, 가격, 이미지 주소
interface interface_props {
  bookNum?: number,
  title?: String,
  author?: String,
  introd?: String,
  price?: number,
  imgUrl?: string,
}

function Card(props: interface_props): React.JSX.Element {
  return (
    <StyledCard>
      <div className="wrap_contents">
        <div className="wrap_img">
          <img src={props.imgUrl} alt="book_img"/>
        </div>
        <div className="book_info">
          <div>
            <p><strong>{props.title}</strong></p>
            <p>{props.author}</p>
            <p>{props.introd}</p>
            <p>{props.price}원</p>
          </div>
        </div>
      </div>
    </StyledCard>
  );
}

export default Card;
