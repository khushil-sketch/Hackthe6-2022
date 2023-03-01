import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';
import picture2 from "./mentorship.tiff"
import {Container,Nav,Navbar,NavDropdown,Button,Card,Row} from 'react-bootstrap';
import { Route, Routes, BrowserRouter } from "react-router-dom";
import Home  from './components/Home/Home'
import MentorSearch from "./components/MentorSearch/MentorSearch";
import ScholarshipSearch from "./components/ScholarshipSearch/ScholarshipSearch";


function App() {
  return (
    <>
    <div className="App" style={{backgroundImage: `url(${picture2})`}}>
  
       <Navbar bg="light" expand="lg">
      <Container>
        
        <Navbar.Brand href="/">
          
        </Navbar.Brand>
        
        
        <Navbar.Toggle aria-controls="basic-navbar-nav" />


        {/*Dropdown Menu */}
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="userprofile">User Profile</Nav.Link>
            <Nav.Link href="about">About</Nav.Link>
            <Nav.Link href="mentorship">Become a Mentor</Nav.Link>
            <Nav.Link href="signup">Sign Up</Nav.Link>
           
            
          </Nav>
        </Navbar.Collapse>

        
      </Container>
    </Navbar>

    


<Container>
  <BrowserRouter>
  <Routes>
       
        
       <Route path="/" element={< Home />} />
       <Route path="/mentorsearch" element={< MentorSearch />}/>
       <Route path="/scholarshipsearch" element={<ScholarshipSearch/>}/>
     </Routes>
  </BrowserRouter>
  
     </Container>
     </div>
    </>
  );
}

export default App;
