import React from 'react';
import styled from "styled-components";

const Main = styled.div`
  width: 45%;
  height: 100%;
  justify-content: center;
  margin: 0 auto;
  background-color: #497dca;
`;

function Home(): React.JSX.Element {
  return (
    <Main>
      <h1>Home</h1>
    </Main>
  );
}

export default Home;

