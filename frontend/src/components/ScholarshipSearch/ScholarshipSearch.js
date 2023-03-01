import { Col,Form, Card, Button} from "react-bootstrap";
import {useState,useEffect} from 'react'

function ScholarshipSearch(){
    const [field, setField] = useState([]);
    return (
<>
<Form>
<Form.Group as={Col} controlId="my_multiselect_field">
      <Form.Label>Which countries do you want to study in?</Form.Label>
      <Form.Control as="select" multiple value={field} onChange={e => setField([].slice.call(e.target.selectedOptions).map(item => item.value))}>
        <option value="field1">Field 1</option>
        <option value="field2">Field 2</option>
        <option value="field3">Field 3</option>
      </Form.Control>
    </Form.Group>

<Form.Group>
<Form.Select aria-label="Default select example">
      <option>What Program</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </Form.Select>
</Form.Group>
<Form.Group>
<Form.Select aria-label="Default select example">
      <option>What University</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </Form.Select>
</Form.Group>

</Form>
</>

    );
}



export default ScholarshipSearch