import "./Footer.css";
import LogoImg from "../../assets/logo.webp";
import { useNavigate } from "react-router-dom";

function Footer() {
  let navigate = useNavigate();

  return (
    <div className="footer" id="footer">
      <div className="footer-bottom">
        <h1
          onClick={() => navigate("/")}
          style={{ cursor: "pointer", fontWeight: "bold", color: "gold" }}
        >
          Reading <span style={{ fontSize: "calc(0.7rem + 1.5vw)" }}>Loop</span>
        </h1>

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
