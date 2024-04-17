import { ThemeProvider, createTheme } from "@mui/material";
// import Content from "./components/Page/Routes";
// // import Header from "./components/Header";
// // import Footer from "./components/Footer";
// // import { BrowserRouter } from "react-router-dom";
// // import { DetectSignLogin } from "./components/DetectSignLogin";
// import Header from "./components/Header";
// import Footer from "./components/Page/Footer";
// import { BrowserRouter } from "react-router-dom";
// // import { DetectSignLogin } from "./components/DetectSignLogin";
// import { DetectSignLogin } from "./components/Page/DetectSignUp";
// import { ToastContainer} from "react-toastify";
// import "react-toastify/dist/ReactToastify.css";

import { BrowserRouter } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import DetectSignLogin from "./page/"
import Header from "./page"
import Content from "./page"
import Footer from "./page"
const theme = createTheme({
  palette: {
    primary: {
      main: "#4b54c5",
    },
  },
  components: {
    MuiPaginationItem: {
      styleOverrides: {
        text: {
          fontSize: "1.3rem",
          fontFamily: "Noto Serif",
        },
      },
    },
  },
});

function App() {
  return (
    <main>
      <BrowserRouter basename="/">
      <ToastContainer
        position="top-center"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover={false}
        theme="colored"
      />
        <ThemeProvider theme={theme}>
          <DetectSignLogin>
            <Header />
          </DetectSignLogin>
          <Content />
          <DetectSignLogin>
            <Footer />
          </DetectSignLogin>
        </ThemeProvider>
      </BrowserRouter>
    </main>
  );
}

export default App;
