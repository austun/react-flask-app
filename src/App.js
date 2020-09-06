import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { brokerService } from "./brokerService";
import BootstrapTable from "react-bootstrap-table-next";

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      address: '',
      error: '',
      brokers: ''
    }

    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.fetchBrokerList = this.fetchBrokerList.bind(this)
  }

  componentDidMount() {
    this.fetchBrokerList()
  }

  fetchBrokerList() {
    brokerService.getBrokers()
    .then(response => {
        this.setState({
          brokers: response
        });
    })
  }


  handleSubmit = (event) => {
    event.preventDefault();

    brokerService.signup(this.state.first_name, this.state.last_name, this.state.email, this.state.address)
      .then(response => {
        if (typeof response.status !== 'undefined' && response.status !== 200) {
          this.setState({ error: response.message });
        } else {
          this.setState({
            first_name: '',
            last_name: '',
            email: '',
            address: '',
            error: ''
          });

          this.fetchBrokerList()
        }
      })

  }

  handleChange = (event) => {
    event.preventDefault();

    this.setState({
      [event.target.name]: event.target.value
    });
  }

  render() {

    const { first_name, last_name, email, address, error, brokers } = this.state;

    const columns = [
      {
        dataField: "title",
        text: "Title"
      },
      {
        dataField: "domain",
        text: "Domain"
      },
      {
        dataField: "first_name",
        text: "First Name"
      },
      {
        dataField: "last_name",
        text: "Last Name"
      },
      {
        dataField: "email",
        text: "Email"
      },
      {
        dataField: "address",
        text: "Address"
      }
    ];

    return (
      <div className="row">
        <div className="col-md-6 offset-md-3">
          <form onSubmit={this.handleSubmit}>
            <h1>Registration For Brokers</h1>

            <div className="form-group">
              <label htmlFor="first_name">First Name</label>
              <input type="text" className="form-control" name="first_name" value={first_name}
                onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label htmlFor="last_name">Last Name</label>
              <input type="text" className="form-control" name="last_name" value={last_name}
                onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="text" className="form-control" name="email"
                value={email} onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label htmlFor="address">Address</label>
              <input type="text" className="form-control" name="address"
                value={address} onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <button className="btn btn-primary btn-lg">Sign Up</button>
            </div>

            {error !== '' && <div className="alert alert-danger">{error}</div>}
          </form>


        </div>
        <div className="col-md-12 offset-md-0">
        <h1 style={{textAlign: "center"}}>List of Brokers</h1>
        <BootstrapTable
            keyField="id"
            data={brokers}
            columns={columns}
            striped
            hover
            condensed
          />
        </div>

      </div>
    );
  }
}

export default App;
