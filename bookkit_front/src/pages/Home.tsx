import React from 'react';
import styled from "styled-components";
import Card from "../components/card/Card.tsx";

const Main = styled.div`
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 0 auto;
  background-color: white;  
`;

interface dummy {
  imgUrl: string
  title: string,
  price: number,
  author: string,
  introd: string,
}

// dummy data
const dummyData:dummy = {
  imgUrl: "https://image.aladin.co.kr/product/34152/44/cover200/k242931499_1.jpg",
  title: "주술회전 26 쿼드러플 특장판",
  price: 6000,
  author: "아쿠타미 게게",
  introd: "역사상 최강의 주술사와 현대 최강의 주술사 세기의 대결전, 절정으로--!"
};

function Home(): React.JSX.Element {
  return (
    <Main>
      <Card bookNum={1} imgUrl={dummyData.imgUrl} title={dummyData.title} price={dummyData.price} author={dummyData.author} introd={dummyData.introd}/>
      <Card bookNum={1} imgUrl={dummyData.imgUrl} title={dummyData.title} price={dummyData.price} author={dummyData.author} introd={dummyData.introd}/>
      <Card bookNum={1} imgUrl={dummyData.imgUrl} title={dummyData.title} price={dummyData.price} author={dummyData.author} introd={dummyData.introd}/>
      <Card bookNum={1} imgUrl={dummyData.imgUrl} title={dummyData.title} price={dummyData.price} author={dummyData.author} introd={dummyData.introd}/>
      <Card bookNum={1} imgUrl={dummyData.imgUrl} title={dummyData.title} price={dummyData.price} author={dummyData.author} introd={dummyData.introd}/>
    </Main>
  );
}

export default Home;
