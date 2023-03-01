import picture1 from "./../../scholarship.jpg"
import picture2 from "./../../mentorship.tiff"
import {Container,Nav,Navbar,NavDropdown,Button,Card,Row} from 'react-bootstrap';

function Home(){

    return (
      
        <>
        <Container className="d-flex vh-100">

<Row className="m-auto align-self-center">
  <Card style={{ width: '18rem' }}>
      <Card.Img variant="bottom" src={picture2}/>
      <Card.Body>
        <Card.Title>Mentorship</Card.Title>
        <Card.Text>
          Connect with a student Mentor
        </Card.Text>
        <Button variant="primary"  href="mentorsearch">Search for Mentorship</Button>
      </Card.Body>
    </Card>

    <Card style={{ width: '18rem' }}>
      <Card.Img variant="bottom" src={picture1}/>
      <Card.Body>
        <Card.Title>Scholarship</Card.Title>
        <Card.Text>
          Find new Scholarships near you
        </Card.Text>
        <Button variant="primary" href="scholarshipsearch">Search for Scholarships</Button>
      </Card.Body>
    </Card>
  </Row>
</Container>
        </>
    );
}

export default Home;

