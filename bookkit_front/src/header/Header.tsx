import React from 'react';
import styled from "styled-components";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faSquareGithub, faSquareInstagram} from "@fortawesome/free-brands-svg-icons";

const HeaderComponent = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-content: center;
  background-color: white;
  padding: 0.6rem 0rem 0.6rem 0rem;
  height: 5rem;

  nav {
    display: flex;
    justify-content: center;
    align-items: center;

    ul {
      display: flex;
      justify-content: center;
      align-content: center;
      flex-direction: row;
      padding: 0;
    }

    li {
      padding: 0px 15px 0px 15px;
      list-style: none;

      a {
        color: black;
        font-size: 1.3rem;
        text-decoration: none;

      }
    }

    .yes:hover {
      color: #0080ff;
    }

    .aladin:hover {
      color: #df2e7f;
    }
  }

  .connects {
    width: 160px;
    height: 85px;
    display: flex;
    justify-content: center;
    align-items: center;

    .con_item > svg {
      height: 3rem;
      width: 3rem;

    }
  }
`;

function Header(): React.JSX.Element {
  return (
    <HeaderComponent>
      <div className="icon_div">
        <img src={"/title.png"}/>
      </div>
      <nav>
        <ul>
          <li>
            <a className="yes"
               href="https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24">Yes 24</a>
          </li>
          <li>
            <a className="aladin" href="https://www.aladin.co.kr/home/welcome.aspx">알라딘</a>
          </li>
        </ul>
      </nav>
      <div className="connects">
        <a className={"con_item"}>
          <FontAwesomeIcon icon={faSquareGithub} />
        </a>
        <a className={"con_item"}>
          <FontAwesomeIcon icon={faSquareInstagram} />
        </a>
      </div>
    </HeaderComponent>
  )
}

export default Header;
