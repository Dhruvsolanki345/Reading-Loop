import "./Footer.css";
import LogoImg from "../../assets/logo.webp";
import { useLocation, useNavigate } from "react-router-dom";

function Footer() {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div
      className="footer"
      style={{ position: location.pathname.length > 10 ? "static":"fixed" }}
      id="footer"
    >
      <div className="footer-bottom">
        {/* <h1
          onClick={() => navigate("/")}
          style={{ cursor: "pointer", fontWeight: "bold", color: "gold" }}
        >
          Reading <span style={{ fontSize: "calc(0.7rem + 1.5vw)" }}>Loop</span>
        </h1> */}
        <h4
          onClick={() => navigate("/")}
          style={{ cursor: "pointer", fontWeight: "bold", color: "gold" }}
        >
          Reading <span style={{ fontSize: "calc(0.7rem + 1.4vw)" }}>Loop</span>
        </h4>

        <div
          style={{
            fontSize: 14,
            textAlign: "center",
          }}
        >
          © 2022 Reading Loop - An online library portal
        </div>
      </div>
    </div>
  );
}

export default Footer;
